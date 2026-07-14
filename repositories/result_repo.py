"""
Result repository - raw SQL for all database operations.
"""
from repositories.base import execute_query, execute_insert_return_id


def insert_result(student_id, course_id, marks_obtained, total_marks):
    """Insert a new result."""
    query = """
        INSERT INTO results (student_id, course_id, marks_obtained, total_marks)
        VALUES (%s, %s, %s, %s)
    """
    params = (student_id, course_id, marks_obtained, total_marks)
    return execute_insert_return_id(query, params)


def fetch_all_results_with_details():
    """Fetch all results with student and course info (JOIN)."""
    query = """
        SELECT r.id, r.student_id, r.course_id, r.marks_obtained, r.total_marks,
               s.name AS student_name, s.email AS student_email,
               c.name AS course_name
        FROM results r
        INNER JOIN students s ON r.student_id = s.id
        INNER JOIN courses c ON r.course_id = c.id
        ORDER BY r.id
    """
    return execute_query(query)


def update_result(result_id, marks_obtained, total_marks):
    """Update an existing result."""
    query = """
        UPDATE results
        SET marks_obtained = %s, total_marks = %s
        WHERE id = %s
    """
    params = (marks_obtained, total_marks, result_id)
    execute_query(query, params, fetch=False)
    return result_id


def delete_result(result_id):
    """Delete a result."""
    query = "DELETE FROM results WHERE id = %s"
    execute_query(query, (result_id,), fetch=False)


def get_result_by_id(result_id):
    """Get single result with details."""
    query = """
        SELECT r.id, r.student_id, r.course_id, r.marks_obtained, r.total_marks,
               s.name AS student_name, c.name AS course_name
        FROM results r
        INNER JOIN students s ON r.student_id = s.id
        INNER JOIN courses c ON r.course_id = c.id
        WHERE r.id = %s
    """
    result = execute_query(query, (result_id,))
    return result[0] if result else None


def search_results_by_student(student_id):
    """Search results by student ID."""
    query = """
        SELECT r.id, r.student_id, r.course_id, r.marks_obtained, r.total_marks,
               s.name AS student_name, c.name AS course_name
        FROM results r
        INNER JOIN students s ON r.student_id = s.id
        INNER JOIN courses c ON r.course_id = c.id
        WHERE r.student_id = %s
        ORDER BY r.id
    """
    return execute_query(query, (student_id,))


def get_dashboard_counts():
    """Get counts for dashboard (SQL aggregation)."""
    from django.db import connection
    counts = {}
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM students")
        counts['students'] = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM courses")
        counts['courses'] = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM results")
        counts['results'] = cursor.fetchone()[0]
    return counts
