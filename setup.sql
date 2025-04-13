-- SQL commands to set up the initial database schema for the application

-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a sample admin user (optional)
INSERT INTO users (username, password, role) VALUES 
('admin', 'hashed_password_here');  -- Replace 'hashed_password_here' with an actual hashed password

-- Create any additional tables as needed for your application
-- For example, if you have a posts table, you could add:
-- CREATE TABLE posts (
--     id SERIAL PRIMARY KEY,
--     user_id INT REFERENCES users(id),
--     content TEXT NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );