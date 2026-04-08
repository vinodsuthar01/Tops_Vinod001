from django.db import models
from django.conf import settings

author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='posts/', null=True, blank=True)  # ✅

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title