"""
Result views - CRUD and search.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services import result_service
from repositories import student_repo, course_repo


@login_required
def result_list(request):
    """List all results. Supports filter by student."""
    student_id = request.GET.get('student_id', '').strip()
    if student_id:
        results = result_service.search_results_by_student(student_id)
    else:
        results = result_service.get_all_results()
    students = student_repo.fetch_all_students_with_course()
    return render(request, 'results/list.html', {
        'results': results,
        'students': students,
        'selected_student_id': student_id,
    })


@login_required
def result_create(request):
    """Create new result."""
    students = student_repo.fetch_all_students_with_course()
    courses = course_repo.fetch_all_courses()
    if request.method == 'POST':
        try:
            result_service.create_result(
                student_id=request.POST.get('student_id'),
                course_id=request.POST.get('course_id'),
                marks_obtained=request.POST.get('marks_obtained'),
                total_marks=request.POST.get('total_marks'),
            )
            messages.success(request, 'Result created successfully.')
            return redirect('results:list')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'results/form.html', {
        'result': None,
        'students': students,
        'courses': courses,
    })


@login_required
def result_update(request, pk):
    """Update existing result."""
    result = result_service.get_result_by_id(pk)
    if not result:
        messages.error(request, 'Result not found.')
        return redirect('results:list')
    students = student_repo.fetch_all_students_with_course()
    courses = course_repo.fetch_all_courses()
    if request.method == 'POST':
        try:
            result_service.update_result(
                result_id=pk,
                marks_obtained=request.POST.get('marks_obtained'),
                total_marks=request.POST.get('total_marks'),
            )
            messages.success(request, 'Result updated successfully.')
            return redirect('results:list')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'results/form.html', {
        'result': result,
        'students': students,
        'courses': courses,
    })


@login_required
def result_delete(request, pk):
    """Delete result."""
    if request.method == 'POST':
        try:
            result_service.delete_result(pk)
            messages.success(request, 'Result deleted successfully.')
        except ValueError as e:
            messages.error(request, str(e))
    return redirect('results:list')
