"""
Student repository - raw SQL for all database operations.
"""
from repositories.base import execute_query, execute_insert_return_id


def insert_student(name, email, gender, course_id=None):
    """Insert a new student."""
    query = """
        INSERT INTO students (name, email, gender, course_id)
        VALUES (%s, %s, %s, %s)
    """
    params = (name, email, gender, course_id)
    return execute_insert_return_id(query, params)


def fetch_all_students_with_course():
    """Fetch all students with course name (JOIN)."""
    query = """
        SELECT s.id, s.name, s.email, s.gender, s.course_id,
               c.name AS course_name
        FROM students s
        LEFT JOIN courses c ON s.course_id = c.id
        ORDER BY s.id
    """
    return execute_query(query)


def update_student(student_id, name, email, gender, course_id=None):
    """Update an existing student."""
    query = """
        UPDATE students
        SET name = %s, email = %s, gender = %s, course_id = %s
        WHERE id = %s
    """
    params = (name, email, gender, course_id, student_id)
    execute_query(query, params, fetch=False)
    return student_id


def delete_student(student_id):
    """Delete a student."""
    query = "DELETE FROM students WHERE id = %s"
    execute_query(query, (student_id,), fetch=False)


def get_student_by_id(student_id):
    """Get single student with course info."""
    query = """
        SELECT s.id, s.name, s.email, s.gender, s.course_id,
               c.name AS course_name
        FROM students s
        LEFT JOIN courses c ON s.course_id = c.id
        WHERE s.id = %s
    """
    result = execute_query(query, (student_id,))
    return result[0] if result else None


def search_students(term):
    """Search students by name or ID."""
    query = """
        SELECT s.id, s.name, s.email, s.gender, s.course_id,
               c.name AS course_name
        FROM students s
        LEFT JOIN courses c ON s.course_id = c.id
        WHERE s.name ILIKE %s OR s.email ILIKE %s
           OR CAST(s.id AS TEXT) = %s
        ORDER BY s.id
    """
    search_pattern = f"%{term}%" if term else "%"
    params = (search_pattern, search_pattern, term or '')
    return execute_query(query, params)
