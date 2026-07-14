# SQL Queries Reference

All queries use parameterized placeholders (`%s`) to prevent SQL injection.

## Students

### Insert
```sql
INSERT INTO students (name, email, gender, course_id)
VALUES (%s, %s, %s, %s)
RETURNING id
```

### Fetch all with course (JOIN)
```sql
SELECT s.id, s.name, s.email, s.gender, s.course_id, c.name AS course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.id
ORDER BY s.id
```

### Update
```sql
UPDATE students
SET name = %s, email = %s, gender = %s, course_id = %s
WHERE id = %s
```

### Delete
```sql
DELETE FROM students WHERE id = %s
```

### Search by name/email/ID
```sql
SELECT s.id, s.name, s.email, s.gender, s.course_id, c.name AS course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.id
WHERE s.name ILIKE %s OR s.email ILIKE %s OR CAST(s.id AS TEXT) = %s
ORDER BY s.id
```

## Courses

### Insert
```sql
INSERT INTO courses (name, duration, fee, description)
VALUES (%s, %s, %s, %s)
RETURNING id
```

### Fetch all
```sql
SELECT id, name, duration, fee, description
FROM courses
ORDER BY id
```

### Update
```sql
UPDATE courses
SET name = %s, duration = %s, fee = %s, description = %s
WHERE id = %s
```

### Delete
```sql
DELETE FROM courses WHERE id = %s
```

## Results

### Insert
```sql
INSERT INTO results (student_id, course_id, marks_obtained, total_marks)
VALUES (%s, %s, %s, %s)
RETURNING id
```

### Fetch all with details (JOIN)
```sql
SELECT r.id, r.student_id, r.course_id, r.marks_obtained, r.total_marks,
       s.name AS student_name, s.email AS student_email, c.name AS course_name
FROM results r
INNER JOIN students s ON r.student_id = s.id
INNER JOIN courses c ON r.course_id = c.id
ORDER BY r.id
```

### Search by student
```sql
SELECT r.id, r.student_id, r.course_id, r.marks_obtained, r.total_marks,
       s.name AS student_name, c.name AS course_name
FROM results r
INNER JOIN students s ON r.student_id = s.id
INNER JOIN courses c ON r.course_id = c.id
WHERE r.student_id = %s
ORDER BY r.id
```

### Percentage (calculated in service layer)
`(marks_obtained / total_marks) * 100`

## Dashboard Aggregation

```sql
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM results;
```
