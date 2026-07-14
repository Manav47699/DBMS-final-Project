"""
Student service - business logic layer.
Converts repository data, validates input, applies transformations.
"""
from repositories import student_repo


def get_all_students():
    """Get all students with course names as structured dicts."""
    rows = student_repo.fetch_all_students_with_course()
    return [_row_to_dict(r) for r in rows]


def get_student_by_id(student_id):
    """Get single student by ID."""
    row = student_repo.get_student_by_id(student_id)
    return _row_to_dict(row) if row else None


def create_student(name, email, gender, course_id=None):
    """Create student with validation."""
    if not name or not name.strip():
        raise ValueError("Name is required")
    if not email or not email.strip():
        raise ValueError("Email is required")
    if not gender or gender not in ('male', 'female', 'other'):
        raise ValueError("Valid gender is required")
    return student_repo.insert_student(
        name.strip(), email.strip().lower(), gender,
        course_id if course_id else None
    )


def update_student(student_id, name, email, gender, course_id=None):
    """Update student with validation."""
    if not student_repo.get_student_by_id(student_id):
        raise ValueError("Student not found")
    if not name or not name.strip():
        raise ValueError("Name is required")
    if not email or not email.strip():
        raise ValueError("Email is required")
    if not gender or gender not in ('male', 'female', 'other'):
        raise ValueError("Valid gender is required")
    return student_repo.update_student(
        student_id, name.strip(), email.strip().lower(), gender,
        course_id if course_id else None
    )


def delete_student(student_id):
    """Delete student."""
    if not student_repo.get_student_by_id(student_id):
        raise ValueError("Student not found")
    student_repo.delete_student(student_id)


def search_students(term):
    """Search students by name, email, or ID."""
    if not term or not str(term).strip():
        return get_all_students()
    rows = student_repo.search_students(str(term).strip())
    return [_row_to_dict(r) for r in rows]


def _row_to_dict(row):
    """Convert repository row to dict with consistent keys."""
    if not row:
        return None
    return {
        'id': row.get('id'),
        'name': row.get('name'),
        'email': row.get('email'),
        'gender': row.get('gender'),
        'course_id': row.get('course_id'),
        'course_name': row.get('course_name') or '—',
    }
