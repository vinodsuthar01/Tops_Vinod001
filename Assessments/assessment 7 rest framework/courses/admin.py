from django.contrib import admin
from courses.models import *
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title","discription"]
admin.site.register(Course, CourseAdmin)
