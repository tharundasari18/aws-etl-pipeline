import boto3
import csv
from io import StringIO
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    if not key.startswith('raw/'):
        return "Skipped"

    print("Processing:", key)

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    input_file = StringIO(content)
    reader = csv.DictReader(input_file)

    print("Columns:", reader.fieldnames)

    output_by_year = {}

    for row in reader:

        # Clean nulls
        for col in row:
            if row[col] == '' or row[col] is None:
                row[col] = 'NA'

        year = row['Year']   # ✅ FIXED HERE

        if year not in output_by_year:
            output_by_year[year] = []

        output_by_year[year].append(row)

    for year, rows in output_by_year.items():

        output_file = StringIO()
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

        s3.put_object(
            Bucket='ipl-clean-trn',
            Key=f'processed/year={year}/ipl_winners_{year}.csv',
            Body=output_file.getvalue()
        )

        print(f"Written partition: year={year}")

    return "Done"
