from rest_framework.viewsets import ModelViewSet
from enrolls.serializers import *
from enrolls.models import *
from rest_framework.response import Response
from rest_framework import status


class EnrollsViewSet(ModelViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

    def create(self, request, *args, **kwargs):
        student = request.data.get('student')
        course = request.data.get('course')

        # 🔥 Check duplicate
        if Enroll.objects.filter(student=student, course=course).exists():
            return Response(
                {"error": "Student already enrolled in this course"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)