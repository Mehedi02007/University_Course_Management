from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.list_courses, name='list_courses'),
    path('students/', views.list_students, name='list_students'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('students/<int:student_id>/',
         views.student_detail, name='student_detail'),
]
