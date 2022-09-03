from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Photo(models.Model):
    """
    Photo model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(
        upload_to='images/', default='../default_post_liudmg', blank=True
    )
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content