-- a script that creates the table `unique_id` on the current database in one's MySQL server
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1,
	UNIQUE(`id`),
	`name` VARCHAR(256)
);
