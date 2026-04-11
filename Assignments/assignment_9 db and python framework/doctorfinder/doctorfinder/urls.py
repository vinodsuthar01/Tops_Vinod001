from django.contrib import admin
from django.urls import path, include
from doctor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add/', views.add_doctor),
    path('delete/<int:id>/', views.delete_doctor),
    path('accounts/', include('allauth.urls')),
]