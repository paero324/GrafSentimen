
CREATE DATABASE IF NOT EXISTS grafsentimen;
USE grafsentimen;

-- Buat tabel users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('gratis', 'premium') DEFAULT 'gratis',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tambahkan user contoh
INSERT INTO users (email, password, role) VALUES
('user1@example.com', SHA2('password123', 256), 'gratis'),
('admin@example.com', SHA2('admin123', 256), 'premium');
