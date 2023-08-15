-- a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in one's MySQL server
-- Retrieves the average of rows using the `score` column in `second_table` table in the current database
SELECT AVG(`score`) AS `average` FROM `second_table`;
