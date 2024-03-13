-- Lists all records in the table second_table with the score >= 10 in the MySQL server.
-- Records are ordered by a descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
