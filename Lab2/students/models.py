from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    courses = models.ManyToManyField(Course, related_name="students")

    def __str__(self):
        return self.name