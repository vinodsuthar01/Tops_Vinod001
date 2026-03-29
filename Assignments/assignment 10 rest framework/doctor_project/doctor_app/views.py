# Create your views here.
from rest_framework import generics
from doctor_app.models import Doctor
from doctor_app.serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]