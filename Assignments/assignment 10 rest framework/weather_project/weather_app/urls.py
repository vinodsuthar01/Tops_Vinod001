from django.urls import path
from weather_app.views import weather_api

urlpatterns = [
    path('weather/', weather_api, name='weather_api'),
]