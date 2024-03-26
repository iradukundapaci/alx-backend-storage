--Use any database
--Adding more attributes
--Drops existing table
DROP TABLE IF EXISTS users;
CREATE TABLE users(
id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
country ENUM('US','CO','TN') DEFAULT='US',
PRIMARY kEY (id)
);