"""
Result service - business logic layer.
Handles percentage calculation, validation.
"""
from repositories import result_repo


def get_all_results():
    """Get all results with student/course info and calculated percentage."""
    rows = result_repo.fetch_all_results_with_details()
    return [_row_to_dict(r) for r in rows]


def get_result_by_id(result_id):
    """Get single result by ID."""
    row = result_repo.get_result_by_id(result_id)
    return _row_to_dict(row) if row else None


def create_result(student_id, course_id, marks_obtained, total_marks):
    """Create result with validation."""
    if not student_id:
        raise ValueError("Student is required")
    if not course_id:
        raise ValueError("Course is required")
    try:
        marks = float(marks_obtained)
        total = float(total_marks)
    except (TypeError, ValueError):
        raise ValueError("Marks must be valid numbers")
    if marks < 0 or total <= 0:
        raise ValueError("Marks must be non-negative; total marks must be positive")
    if marks > total:
        raise ValueError("Marks obtained cannot exceed total marks")
    return result_repo.insert_result(int(student_id), int(course_id), marks, total)


def update_result(result_id, marks_obtained, total_marks):
    """Update result with validation."""
    if not result_repo.get_result_by_id(result_id):
        raise ValueError("Result not found")
    try:
        marks = float(marks_obtained)
        total = float(total_marks)
    except (TypeError, ValueError):
        raise ValueError("Marks must be valid numbers")
    if marks < 0 or total <= 0:
        raise ValueError("Marks must be non-negative; total marks must be positive")
    if marks > total:
        raise ValueError("Marks obtained cannot exceed total marks")
    return result_repo.update_result(result_id, marks, total)


def delete_result(result_id):
    """Delete result."""
    if not result_repo.get_result_by_id(result_id):
        raise ValueError("Result not found")
    result_repo.delete_result(result_id)


def search_results_by_student(student_id):
    """Search results by student ID."""
    if not student_id:
        return get_all_results()
    rows = result_repo.search_results_by_student(int(student_id))
    return [_row_to_dict(r) for r in rows]


def get_dashboard_counts():
    """Get aggregated counts for dashboard."""
    return result_repo.get_dashboard_counts()


def _calculate_percentage(marks_obtained, total_marks):
    """Calculate percentage. Returns 0 if total is 0."""
    try:
        marks = float(marks_obtained or 0)
        total = float(total_marks or 0)
        if total <= 0:
            return 0
        return round((marks / total) * 100, 2)
    except (TypeError, ValueError):
        return 0


def _row_to_dict(row):
    """Convert repository row to dict with percentage."""
    if not row:
        return None
    marks = float(row.get('marks_obtained') or 0)
    total = float(row.get('total_marks') or 0)
    return {
        'id': row.get('id'),
        'student_id': row.get('student_id'),
        'course_id': row.get('course_id'),
        'marks_obtained': marks,
        'total_marks': total,
        'percentage': _calculate_percentage(marks, total),
        'student_name': row.get('student_name'),
        'course_name': row.get('course_name'),
        'student_email': row.get('student_email'),
    }
