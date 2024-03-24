from django.shortcuts import render
from .models import Student, Course


def index(request):
    return render(request, 'index.html')


def list_students(request):
    students = Student.objects.all()
    return render(request, 'student_courses/list_students.html', {'students': students})


def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'student_courses/list_courses.html', {'courses': courses})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    total_students = students.count()
    context = {
        'course': course,
        'students': students,
        'total_students': total_students
    }
    return render(request, 'student_courses/course_detail.html', context)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student
    }
    return render(request, 'student_courses/student_detail.html', context)
