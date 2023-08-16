-- a script that creates the database `hbtn_0d_usa` in one's MySQL server
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- and creates the table `states` (in the database `hbtn_0d_usa`)
USE `hbtn_0d_usa`
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL
);
