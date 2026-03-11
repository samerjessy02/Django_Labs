from django.shortcuts import render, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, "students/students_list.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    return render(request, "students/student_detail.html", {
        "student": student
    })

# from django.shortcuts import render, get_object_or_404
# from .models import Student

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, "students/students_list.html", {"students": students})


# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     # Get all courses this student is enrolled in
#     courses = student.courses.all()

#     return render(request, "students/student_detail.html", {
#         "student": student,
#         "courses": courses
#     })