from django.urls import path
from doctor_profile_app.views import *


urlpatterns = [
    path('',home_page,name='home_page'),
    path('profile/<int:id>',profile_page,name='profile_page'),
    path('patient_reg/',patient_reg,name ="patient_reg"),
    path('patient/',patient_list,name="patient"),
    path('about/',about_us,name="about"),
    path('signup/',sign_up_page,name="signup"),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name="logout"),
    path('delete/<int:id>/',delete,name="delete"),
    path('edit/<int:id>/',edit,name="edit"),
    path('edit_profile/<int:id>/',edit_profile,name="edit_profile")
]