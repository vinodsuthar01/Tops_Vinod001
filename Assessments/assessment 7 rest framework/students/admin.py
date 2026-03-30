from django.contrib import admin
from students.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","age"]
admin.site.register(Student,StudentAdmin)
