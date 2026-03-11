from django.shortcuts import render
from .models import Instructor

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors/instructors_list.html", {"instructors": instructors})