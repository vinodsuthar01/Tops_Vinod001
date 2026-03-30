from rest_framework.viewsets import ModelViewSet
from students.serializers import *
from students.models import *


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer