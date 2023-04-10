-- Creating my first table
-- In the current database specified to the mysql call
-- Usage < cat name_of_file.sql | mysql -u root -p database>
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
