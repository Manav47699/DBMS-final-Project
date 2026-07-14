"""
Course repository - raw SQL for all database operations.
"""
from repositories.base import execute_query, execute_insert_return_id


def insert_course(name, duration, fee=0, description=''):
    """Insert a new course."""
    query = """
        INSERT INTO courses (name, duration, fee, description)
        VALUES (%s, %s, %s, %s)
    """
    params = (name, duration, fee, description)
    return execute_insert_return_id(query, params)


def fetch_all_courses():
    """Fetch all courses."""
    query = """
        SELECT id, name, duration, fee, description
        FROM courses
        ORDER BY id
    """
    return execute_query(query)


def update_course(course_id, name, duration, fee=0, description=''):
    """Update an existing course."""
    query = """
        UPDATE courses
        SET name = %s, duration = %s, fee = %s, description = %s
        WHERE id = %s
    """
    params = (name, duration, fee, description, course_id)
    execute_query(query, params, fetch=False)
    return course_id


def delete_course(course_id):
    """Delete a course."""
    query = "DELETE FROM courses WHERE id = %s"
    execute_query(query, (course_id,), fetch=False)


def get_course_by_id(course_id):
    """Get single course by ID."""
    query = "SELECT id, name, duration, fee, description FROM courses WHERE id = %s"
    result = execute_query(query, (course_id,))
    return result[0] if result else None
