from django.db import models
from . import User, Post


class Like(models.Model):
    """Block"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)