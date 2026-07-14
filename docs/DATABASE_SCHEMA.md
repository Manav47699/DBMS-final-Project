# Database Schema

## Entity-Relationship Diagram

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│    courses      │       │    students     │       │    results      │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ id (PK)         │◄──────│ course_id (FK)  │       │ id (PK)         │
│ name            │       │ id (PK)         │◄──────│ student_id (FK) │
│ duration        │       │ name            │       │ course_id (FK)  │──┐
│ fee             │       │ email (unique)  │       │ marks_obtained  │  │
│ description     │       │ gender          │       │ total_marks     │  │
└─────────────────┘       └─────────────────┘       └─────────────────┘  │
        │                           │                         │           │
        └───────────────────────────┴─────────────────────────┘───────────┘
```

## Relationships

- **One Course → Many Students**: A course can have many enrolled students
- **One Student → Many Results**: A student can have results in multiple courses
- **One Course → Many Results**: A course can have many result records

## Tables

### courses
| Column     | Type          | Constraints                |
|------------|---------------|----------------------------|
| id         | SERIAL        | PRIMARY KEY                |
| name       | VARCHAR(200)  | NOT NULL                   |
| duration   | VARCHAR(100)  | NOT NULL                   |
| fee        | DECIMAL(10,2) | DEFAULT 0                  |
| description| TEXT          | DEFAULT ''                 |

### students
| Column    | Type         | Constraints                |
|-----------|--------------|----------------------------|
| id        | SERIAL       | PRIMARY KEY                |
| name      | VARCHAR(200) | NOT NULL                   |
| email     | VARCHAR(254) | UNIQUE, NOT NULL           |
| gender    | VARCHAR(20)  | CHECK (male/female/other)  |
| course_id | INTEGER      | FK → courses(id), SET NULL |

### results
| Column         | Type          | Constraints                    |
|----------------|---------------|--------------------------------|
| id             | SERIAL        | PRIMARY KEY                    |
| student_id     | INTEGER       | FK → students(id), CASCADE     |
| course_id      | INTEGER       | FK → courses(id), CASCADE      |
| marks_obtained | DECIMAL(6,2)  | NOT NULL, >= 0                 |
| total_marks    | DECIMAL(6,2)  | NOT NULL, > 0                  |

**Unique constraint:** (student_id, course_id)

## Indexes

- `idx_students_course_id` on students(course_id)
- `idx_results_student_id` on results(student_id)
- `idx_results_course_id` on results(course_id)
- `idx_students_email` on students(email)
- `idx_students_name` on students(name)
