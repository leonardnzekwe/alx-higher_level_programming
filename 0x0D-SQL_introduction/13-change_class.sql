-- a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in one's MySQL server
-- Deletes `second_table` table rows with values in `score` <= 5 in the current database
DELETE FROM `second_table` WHERE `score` <= 5;
