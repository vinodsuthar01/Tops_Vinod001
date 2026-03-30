from rest_framework.viewsets import ModelViewSet
from courses.serializers import *
from courses.models import *


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer