from django.db import models
from instructors.models import Instructor

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="courses/", null=True, blank=True)

    def __str__(self):
        return self.title