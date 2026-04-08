from django.contrib import admin
from interactions.models import *

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'content', 'created_at']
    search_fields = ['user',]

class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower','following']
    search_fields = ['follower','following']


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']
    search_fields = ['user',]



admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Like, LikeAdmin)
