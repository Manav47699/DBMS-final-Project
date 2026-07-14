"""
Course views - CRUD.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services import course_service


@login_required
def course_list(request):
    """List all courses."""
    courses = course_service.get_all_courses()
    return render(request, 'courses/list.html', {'courses': courses})


@login_required
def course_create(request):
    """Create new course."""
    if request.method == 'POST':
        try:
            course_service.create_course(
                name=request.POST.get('name'),
                duration=request.POST.get('duration'),
                fee=request.POST.get('fee') or 0,
                description=request.POST.get('description') or '',
            )
            messages.success(request, 'Course created successfully.')
            return redirect('courses:list')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'courses/form.html', {'course': None})


@login_required
def course_update(request, pk):
    """Update existing course."""
    course = course_service.get_course_by_id(pk)
    if not course:
        messages.error(request, 'Course not found.')
        return redirect('courses:list')
    if request.method == 'POST':
        try:
            course_service.update_course(
                course_id=pk,
                name=request.POST.get('name'),
                duration=request.POST.get('duration'),
                fee=request.POST.get('fee') or 0,
                description=request.POST.get('description') or '',
            )
            messages.success(request, 'Course updated successfully.')
            return redirect('courses:list')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'courses/form.html', {'course': course})


@login_required
def course_delete(request, pk):
    """Delete course."""
    if request.method == 'POST':
        try:
            course_service.delete_course(pk)
            messages.success(request, 'Course deleted successfully.')
        except ValueError as e:
            messages.error(request, str(e))
    return redirect('courses:list')
