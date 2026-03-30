from django.db import models
from students.models import Student
from courses.models import Course

# Create your models here.
class Enroll(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date_join = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student','course']

    def __str__(self):
        return f"{self.student} - {self.course}"

    