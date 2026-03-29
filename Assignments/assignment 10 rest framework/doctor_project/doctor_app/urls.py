from django.urls import path
from doctor_app.views import DoctorListCreateView, DoctorDetailView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),
]