# DBMS-final-Project

> Our project for Database Management System, 5th semester, Computer Engineering

# Student Result Management System (SRMS)

A full-featured Student Result Management System built with Django, PostgreSQL, and raw SQL. Demonstrates layered architecture, clean separation of concerns, and production-ready database design.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  View Layer (Django Views) - HTTP handling, input validation     │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  Service Layer - Business logic, validation, transformations     │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  Repository Layer - Raw SQL via connection.cursor()              │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  Database (PostgreSQL)                                           │
└─────────────────────────────────────────────────────────────────┘
```

## Project Structure

```
project_root/
├── core/                 # Django project settings
├── apps/
│   ├── accounts/         # Authentication (login/logout)
│   ├── students/
│   ├── courses/
│   └── results/
├── services/             # Business logic
│   ├── student_service.py
│   ├── course_service.py
│   └── result_service.py
├── repositories/         # Raw SQL queries
│   ├── base.py
│   ├── student_repo.py
│   ├── course_repo.py
│   └── result_repo.py
├── templates/
├── sql/                  # Manual schema scripts
└── docs/                 # Documentation
```

## Features

- **Authentication**: Django's built-in auth (login/logout, session management)
- **Dashboard**: Aggregated counts (students, courses, results) via SQL
- **Students**: CRUD, search by name/email/ID, course association
- **Courses**: CRUD
- **Results**: CRUD, filter by student, percentage calculation
- **Security**: Parameterized queries, CSRF protection, login-required decorators

## Setup

### 1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Database

**PostgreSQL (recommended):**

```bash
# Create database
createdb srms_db

# Optional: Run manual schema
psql srms_db < sql/schema.sql

# Configure (or use defaults)
export DB_NAME=srms_db
export DB_USER=postgres
export DB_PASSWORD=postgres
export DB_HOST=localhost
export DB_PORT=5432
```

**SQLite (for quick testing):**

```bash
export USE_SQLITE=true
```

### 3. Migrations

```bash
python manage.py migrate
```

### 4. Create admin user

```bash
python manage.py createsuperuser
```

### 5. Run server

```bash
# With PostgreSQL (default)
python manage.py runserver

# With SQLite
USE_SQLITE=true python manage.py runserver
```

Visit http://127.0.0.1:8000/accounts/login/ and log in.

## Usage

- **Login**: `/accounts/login/` — Use superuser credentials
- **Dashboard**: `/` — Overview counts
- **Students**: `/students/` — List, create, edit, delete, search
- **Courses**: `/courses/` — List, create, edit, delete
- **Results**: `/results/` — List, create, edit, delete, filter by student

## Documentation

- [Database Schema & ER Diagram](docs/DATABASE_SCHEMA.md)
- [SQL Queries Reference](docs/SQL_QUERIES.md)
- [System Flow](docs/SYSTEM_FLOW.md)

## Testing

```bash
python manage.py test
```

## Tech Stack

- **Backend**: Django 6.x
- **Database**: PostgreSQL (SQLite fallback)
- **Data Access**: Raw SQL via `connection.cursor()` (no ORM for core operations)
- **Frontend**: Django templates, Tailwind CSS (CDN)
