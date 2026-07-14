"""
Result model - used only for Django migrations to create table schema.
All CRUD operations use raw SQL via repositories.
"""
from django.db import models


class Result(models.Model):
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='results',
        db_column='student_id'
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='results',
        db_column='course_id'
    )
    marks_obtained = models.DecimalField(max_digits=6, decimal_places=2)
    total_marks = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'results'
        unique_together = [['student', 'course']]

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
