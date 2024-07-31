-- Create the database
CREATE DATABASE IF NOT EXISTS user_info;

-- Use the created database
USE user_info;

-- Create the table for storing user data
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    blood_group VARCHAR(10),
    location VARCHAR(255),
    hobbies TEXT
);
