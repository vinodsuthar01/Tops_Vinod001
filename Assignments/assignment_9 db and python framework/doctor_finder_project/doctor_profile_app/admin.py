from django.contrib import admin
from doctor_profile_app.models import *

# Register your models here.
class PatientRegisterAdmin(admin.ModelAdmin ):
    list_display = ['name','email','age']
    search_fields =[ 'name','email']


class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ['specialization','experience', 'clinic_address','phone']

admin.site.register(PatientRegister,PatientRegisterAdmin)
admin.site.register(DoctorProfile,DoctorProfileAdmin)



