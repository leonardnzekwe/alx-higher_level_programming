-- A script that lists all the tables of a database in one's MySQL server
-- Query to list all the tables of the current database
SELECT TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = (SELECT DATABASE());
