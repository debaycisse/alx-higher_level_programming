-- This script creates a database, named hbtn_0d_usa and a table, named statesinside the just created database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
