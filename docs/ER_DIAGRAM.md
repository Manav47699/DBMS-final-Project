# Entity-Relationship Diagram

## Visual ER Diagram

```
                    ┌──────────────────────────┐
                    │        courses           │
                    ├──────────────────────────┤
                    │ id (PK)         SERIAL   │
                    │ name            VARCHAR  │
                    │ duration        VARCHAR  │
                    │ fee             DECIMAL  │
                    │ description     TEXT     │
                    └────────┬─────────────────┘
                             │
                             │ 1
                             │
                             │ *
                    ┌────────▼─────────────────┐
                    │       students           │
                    ├──────────────────────────┤
                    │ id (PK)         SERIAL   │
                    │ name            VARCHAR  │
                    │ email           VARCHAR  │ (unique)
                    │ gender          VARCHAR  │
                    │ course_id (FK)  INT      │──────────┐
                    └────────┬─────────────────┘          │
                             │                            │
                             │ 1                          │
                             │                            │
                             │ *                          │
                    ┌────────▼─────────────────┐          │
                    │        results           │          │
                    ├──────────────────────────┤          │
                    │ id (PK)         SERIAL   │          │
                    │ student_id (FK) INT      │          │
                    │ course_id (FK)  INT      │──────────┘
                    │ marks_obtained  DECIMAL  │
                    │ total_marks     DECIMAL  │
                    └──────────────────────────┘

Relationships:
- Course 1 ────── * Student  (one course, many students)
- Student 1 ───── * Result   (one student, many results)
- Course 1 ────── * Result   (one course, many results)
```

## Cardinality

| From     | To       | Relationship | Description                    |
|----------|----------|--------------|--------------------------------|
| courses  | students | 1 : N        | One course has many students   |
| students | results  | 1 : N        | One student has many results   |
| courses  | results  | 1 : N        | One course has many results    |
