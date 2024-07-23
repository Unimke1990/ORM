-- Active: 1721511998902@@127.0.0.1@3306@testdb2
CREATE DATABASE testdb2

USE testdb2;

DROP TABLE UsersAndPosts

CREATE TABLE IF NOT EXISTS UsersAndPosts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    gender VARCHAR(20) NOT NULL,
    title VARCHAR(50),
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)


SELECT * FROM UsersAndPosts

INSERT INTO UsersAndPosts (name, email, gender, title, content) 
VALUES ('joe don', 'joedon@gmail.com', 'male', 'My First Post', 'Hello, world!');

INSERT INTO UsersAndPosts (name, email, gender, title, content) VALUES ('jenny eboh', 'jennyeb@gmail.com', 'female', 'welcome', 'hello, i am happy to be here');

DROP TABLE UsersAndPosts

SHOW TABLES;

SELECT * FROM UsersAndPosts
