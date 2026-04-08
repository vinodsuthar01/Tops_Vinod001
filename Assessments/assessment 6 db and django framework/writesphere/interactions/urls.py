from django.urls import path
from interactions.views import *

urlpatterns = [
    path('like/<int:post_id>/', toggle_like, name='like'),
    path('comment/<int:post_id>/', add_comment, name='comment'),
    path('follow/<int:user_id>/', toggle_follow, name='follow'),
    path('comment/edit/<int:id>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:id>/', delete_comment, name='delete_comment'),
]