-- A script that converts `hbtn_0c_0` database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in one's MySQL server

-- Changes the default character-set and collation of the `hbtn_0c_0` database to utf8mb4 and utf8mb4_unicode_ci collation, respectively
-- New tables or fields created in the `hbtn_0c_0 database will use the new encoding
ALTER DATABASE `hbtn_0c_0`
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Converts the existing `first_table` table to use the utf8mb4 character-set and utf8mb4_unicode_ci collation
-- New fields added to the `first_table` table will use the new encoding
ALTER TABLE hbtn_0c_0.first_table CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Modifies the `name` field in the `first_table` table to use the utf8mb4 character-set and utf8mb4_unicode_ci collation
-- The `name` field will adopt the new encoding
ALTER TABLE hbtn_0c_0.first_table
MODIFY `name` VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
