-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in one's MySQL server
-- Retrieves the `score`, distinct count of `score` as `number` from `second_table` table in the current database and sort them in DESC
SELECT `score`, COUNT(*) AS `number` FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;
