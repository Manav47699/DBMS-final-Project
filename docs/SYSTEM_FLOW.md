# System Flow

## Authentication Flow

```
User → Login Page → POST credentials → Django Auth → Session Created
                                              ↓
User ← Dashboard ← Redirect (if valid) ←──────┘
```

## Application Flow

```
Login → Dashboard (aggregated counts)
         │
         ├── Students
         │     ├── List (with search)
         │     ├── Create
         │     ├── Update
         │     └── Delete
         │
         ├── Courses
         │     ├── List
         │     ├── Create
         │     ├── Update
         │     └── Delete
         │
         └── Results
               ├── List (with filter by student)
               ├── Create
               ├── Update
               └── Delete
```

## Request Flow (Layered Architecture)

```
HTTP Request
    ↓
View Layer (Django Views)
    - Validate request
    - Extract POST/GET data
    ↓
Service Layer (Business Logic)
    - Validate data
    - Apply transformations
    - Calculate derived values (e.g., percentage)
    ↓
Repository Layer (Raw SQL)
    - Execute parameterized queries
    - Return raw results
    ↓
Database (PostgreSQL)
```

## Example: Creating a Result

1. **View** receives POST with student_id, course_id, marks_obtained, total_marks
2. **Service** validates: marks >= 0, total > 0, marks <= total
3. **Repository** executes: `INSERT INTO results (...) VALUES (%s, %s, %s, %s) RETURNING id`
4. **Service** returns new ID to view
5. **View** redirects to result list with success message
