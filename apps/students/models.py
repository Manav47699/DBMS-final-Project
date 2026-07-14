"""
Student model - used only for Django migrations to create table schema.
All CRUD operations use raw SQL via repositories.
"""
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        db_column='course_id'
    )

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.name
