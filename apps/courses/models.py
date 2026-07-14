"""
Course model - used only for Django migrations to create table schema.
All CRUD operations use raw SQL via repositories.
"""
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name
