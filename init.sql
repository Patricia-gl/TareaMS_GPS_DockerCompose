CREATE DATABASE IF NOT EXISTS dbbtarea;
USE dbbtarea;

CREATE TABLE IF NOT EXISTS estudiante (
    rut VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    curso VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS evaluacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(20),
    semestre VARCHAR(20),
    asignatura VARCHAR(100),
    nota FLOAT,
    FOREIGN KEY (rut) REFERENCES estudiante(rut)
);