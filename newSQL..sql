CREATE DATABASE TestDB;

USE TestDB;

CREATE TABLE IF NOT EXISTS `users` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(20)  NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
)

CREATE TABLE IF NOT EXISTS `posts` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    author_id INT,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES `users`(id)
);

INSERT INTO users(name, gender, email) VALUES ('agim given', 'male', 'agimu@gmail.com')

INSERT INTO posts(title, content) VALUES ('first post', 'hello everyone')

UPDATE posts SET author_id = 1 WHERE id=1;

DROP TABLE users;

SHOW TABLES;

SELECT * FROM posts;


SELECT * FROM users;