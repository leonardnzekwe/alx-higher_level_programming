-- a script that lists all records of the table second_table of the database hbtn_0c_0 in one's MySQL server
-- Retrieves rows with `name` value in the `second_table` table in the current database and sort them in descending order
SELECT `score`, `name` FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
