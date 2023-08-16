-- a script that creates the database `hbtn_0d_usa` in one's MySQL server
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- and creates the table `cities` (in the database hbtn_0d_usa)
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`state_id` INT NOT NULL,
	FOREIGN KEY (`state_id`) REFERENCES `states` (`id`),
	`name` VARCHAR(256) NOT NULL
);
