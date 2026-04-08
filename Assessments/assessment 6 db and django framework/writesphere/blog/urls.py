from django.urls import path
from blog.views import *

urlpatterns = [
    path('',home, name='home'),
    path('post/<int:id>/',detail, name='detail'),
    path('create/',create, name='create'),
    path('update/<int:id>/',update, name='update'),
    path('delete/<int:id>/',delete, name='delete'),
]