from django.contrib import admin
from doctor.models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'location')

admin.site.register(Doctor, DoctorAdmin)