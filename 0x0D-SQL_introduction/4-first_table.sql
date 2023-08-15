-- a script that creates a table called first_table in the current database in one's MySQL server
-- Create the table first_table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
