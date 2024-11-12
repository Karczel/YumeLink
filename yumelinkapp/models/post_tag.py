from django.db import models
from . import Tag, Post


class PostTag(models.Model):
    """Block"""
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)