-- Lists all the records that have score greater or equal to 10 ordered still with top score priority.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;