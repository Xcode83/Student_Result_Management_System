from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class StudentClass(models.Model):
    class_name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.class_name} - {self.section}"

    class Meta:
        verbose_name_plural = "Student Classes"
        unique_together = ('class_name', 'section')

class Subject(models.Model):
    subject_code = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.subject_name} ({self.subject_code})"

class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.roll_number})"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    class Meta:
        unique_together = ('student', 'subject')

    def get_grade(self):
        if self.marks_obtained >= 90: return 'O'
        if self.marks_obtained >= 80: return 'A+'
        if self.marks_obtained >= 70: return 'A'
        if self.marks_obtained >= 60: return 'B'
        if self.marks_obtained >= 50: return 'C'
        return 'F'

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.subject_name}"
