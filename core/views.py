"""
Dashboard view.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from services.result_service import get_dashboard_counts


@login_required
def dashboard(request):
    """Dashboard with aggregated analytics."""
    counts = get_dashboard_counts()
    return render(request, 'dashboard.html', {
        'total_students': counts.get('students', 0),
        'total_courses': counts.get('courses', 0),
        'total_results': counts.get('results', 0),
    })
