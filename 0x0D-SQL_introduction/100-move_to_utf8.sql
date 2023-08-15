-- A script that converts `hbtn_0c_0` database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in one's MySQL server
-- Converts the existing `first_table` table to use the utf8mb4 character-set and utf8mb4_unicode_ci collation
ALTER TABLE hbtn_0c_0.first_table CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
