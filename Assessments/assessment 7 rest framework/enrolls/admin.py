from django.contrib import admin
from enrolls.models import *
# Register your models here.
class EnrollAdmin(admin.ModelAdmin):
    list_display = ["id","student","course","date_join"]
admin.site.register(Enroll, EnrollAdmin)
