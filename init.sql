CREATE DATABASE IF NOT EXISTS logindb;
USE logindb;
CREATE TABLE IF NOT EXISTS accounts(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username varchar(50) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    email varchar(50) NOT NULL UNIQUE
);