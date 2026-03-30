from rest_framework import serializers
from students.models import *
from enrolls.models import *

class StudentSerializer(serializers.ModelSerializer):

    courses = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'age', 'courses']

    def get_courses(self, obj):
        enrollments = Enroll.objects.filter(student=obj)
        return [en.course.title for en in enrollments]