-- Student Result Management System - Database Schema
-- Execute this script to create the database manually for PostgreSQL

-- Create database (run as superuser)
-- CREATE DATABASE srms_db;
-- \c srms_db

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    duration VARCHAR(100) NOT NULL,
    fee DECIMAL(10, 2) DEFAULT 0,
    description TEXT DEFAULT ''
);

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    gender VARCHAR(20) NOT NULL CHECK (gender IN ('male', 'female', 'other')),
    course_id INTEGER REFERENCES courses(id) ON DELETE SET NULL
);

-- Results table
CREATE TABLE IF NOT EXISTS results (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    marks_obtained DECIMAL(6, 2) NOT NULL,
    total_marks DECIMAL(6, 2) NOT NULL,
    UNIQUE(student_id, course_id),
    CHECK (marks_obtained >= 0),
    CHECK (total_marks > 0),
    CHECK (marks_obtained <= total_marks)
);

-- Performance indexes
CREATE INDEX IF NOT EXISTS idx_students_course_id ON students(course_id);
CREATE INDEX IF NOT EXISTS idx_results_student_id ON results(student_id);
CREATE INDEX IF NOT EXISTS idx_results_course_id ON results(course_id);
CREATE INDEX IF NOT EXISTS idx_students_email ON students(email);
CREATE INDEX IF NOT EXISTS idx_students_name ON students(name);
