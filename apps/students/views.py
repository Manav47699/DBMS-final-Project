"""
Student views - CRUD and search.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services import student_service
from repositories import course_repo


@login_required
def student_list(request):
    """List all students. Supports search."""
    search = request.GET.get('search', '').strip()
    if search:
        students = student_service.search_students(search)
    else:
        students = student_service.get_all_students()
    return render(request, 'students/list.html', {
        'students': students,
        'search': search,
    })


@login_required
def student_create(request):
    """Create new student."""
    courses = course_repo.fetch_all_courses()
    if request.method == 'POST':
        try:
            student_service.create_student(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                gender=request.POST.get('gender'),
                course_id=request.POST.get('course_id') or None,
            )
            messages.success(request, 'Student created successfully.')
            return redirect('students:list')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'students/form.html', {
        'courses': courses,
        'student': None,
    })


@login_required
def student_update(request, pk):
    """Update existing student."""
    student = student_service.get_student_by_id(pk)
    if not student:
        messages.error(request, 'Student not found.')
        return redirect('students:list')
    courses = course_repo.fetch_all_courses()
    if request.method == 'POST':
        try:
            student_service.update_student(
                student_id=pk,
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                gender=request.POST.get('gender'),
                course_id=request.POST.get('course_id') or None,
            )
            messages.success(request, 'Student updated successfully.')
            return redirect('students:list')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'students/form.html', {
        'student': student,
        'courses': courses,
    })


@login_required
def student_delete(request, pk):
    """Delete student."""
    if request.method == 'POST':
        try:
            student_service.delete_student(pk)
            messages.success(request, 'Student deleted successfully.')
        except ValueError as e:
            messages.error(request, str(e))
    return redirect('students:list')
