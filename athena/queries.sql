CREATE EXTERNAL TABLE ipl_winners (...); ## You have to choose the column name that has to display on extrnal table.

MSCK REPAIR TABLE ipl_winners;

SELECT * FROM ipl_winners WHERE year='2015';
