-- Active: 1721511998902@@127.0.0.1@3306@testdb
CREATE DATABASE TestDB;

USE TestDB;

CREATE TABLE IF NOT EXISTS `users` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(20)  NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `posts` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    author_id INT,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES `users`(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE users;

DROP TABLE posts;

INSERT INTO users(name, gender, email) VALUES ('agim given', 'male', 'agimu@gmail.com')

INSERT INTO users(name, gender, email) VALUES ('jane umoh', 'female', 'umohjane@yahoo.com')

INSERT INTO users(name, gender, email) VALUES ('dell florence', 'female', 'dellflo@gmail.com')

INSERT INTO posts(author_id, title, content) VALUES (1, 'first post', 'hello everyone')

INSERT INTO posts(author_id, title, content) VALUES (1, 'Hell Dell', 'Nice to be in this file')

INSERT INTO posts(author_id, title, content) VALUES (3, 'flash', 'check the out')

SELECT users.name, users.gender, posts.title, posts.content
FROM users
JOIN posts ON posts.author_id = users.id

UPDATE posts 
SET id = 5 
WHERE created_at = '2024-07-23 14:58:03';

UPDATE users SET id = 3 WHERE id=4;

UPDATE users
SET name = 'simon florence'
WHERE name = 'dell florence'

DELETE FROM users
WHERE name = 'jane umoh'

DELETE FROM posts 
WHERE id=9


SHOW TABLES;

SELECT * FROM posts;

SELECT * FROM users;