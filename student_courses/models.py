from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100)
    max_size = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
