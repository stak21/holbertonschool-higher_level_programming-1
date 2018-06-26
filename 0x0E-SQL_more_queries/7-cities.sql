-- This creates a database hbtn_0d_usa
-- and also table cities in the hbtn_0d_usa datatbase
-- with id INT auto genereated with unique,
-- state_id INT can't be null and inherit from states table,
-- name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
