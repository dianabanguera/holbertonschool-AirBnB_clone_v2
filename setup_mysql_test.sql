-- create a database
CREATE DATABASE if not exists hbnb_test_db;
-- create user
CREATE USER if not exists 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- all privileges
GRANT ALL privileges on hbnb_test_db.* to 'hbnb_test'@'localhost';
-- select privilege
GRANT SELECT on performance_schema.* to 'hbnb_test'@'localhost';
