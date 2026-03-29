from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PatientRegister(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name
    


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    clinic_address = models.TextField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="doctor_images/" ,blank=True,null=True)

    def __str__(self):
        return f"Dr. {self.user.username}"