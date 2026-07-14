"""
Course service - business logic layer.
"""
from repositories import course_repo


def get_all_courses():
    """Get all courses as structured dicts."""
    rows = course_repo.fetch_all_courses()
    return [_row_to_dict(r) for r in rows]


def get_course_by_id(course_id):
    """Get single course by ID."""
    row = course_repo.get_course_by_id(course_id)
    return _row_to_dict(row) if row else None


def create_course(name, duration, fee=0, description=''):
    """Create course with validation."""
    if not name or not name.strip():
        raise ValueError("Name is required")
    if not duration or not str(duration).strip():
        raise ValueError("Duration is required")
    try:
        fee = float(fee) if fee is not None else 0
        if fee < 0:
            raise ValueError("Fee cannot be negative")
    except (TypeError, ValueError):
        fee = 0
    return course_repo.insert_course(
        name.strip(), str(duration).strip(), fee,
        str(description).strip() if description else ''
    )


def update_course(course_id, name, duration, fee=0, description=''):
    """Update course with validation."""
    if not course_repo.get_course_by_id(course_id):
        raise ValueError("Course not found")
    if not name or not name.strip():
        raise ValueError("Name is required")
    if not duration or not str(duration).strip():
        raise ValueError("Duration is required")
    try:
        fee = float(fee) if fee is not None else 0
        if fee < 0:
            raise ValueError("Fee cannot be negative")
    except (TypeError, ValueError):
        fee = 0
    return course_repo.update_course(
        course_id, name.strip(), str(duration).strip(), fee,
        str(description).strip() if description else ''
    )


def delete_course(course_id):
    """Delete course."""
    if not course_repo.get_course_by_id(course_id):
        raise ValueError("Course not found")
    course_repo.delete_course(course_id)


def _row_to_dict(row):
    """Convert repository row to dict."""
    if not row:
        return None
    return {
        'id': row.get('id'),
        'name': row.get('name'),
        'duration': row.get('duration'),
        'fee': float(row.get('fee') or 0),
        'description': row.get('description') or '',
    }
