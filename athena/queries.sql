CREATE EXTERNAL TABLE ipl_winners (...); ##have to specify which columns you have to choose and create in external table

MSCK REPAIR TABLE ipl_winners;

SELECT * FROM ipl_winners WHERE year='2015';
