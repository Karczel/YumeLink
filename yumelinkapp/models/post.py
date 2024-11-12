from django.db import models
from . import User


class Post(models.Model):
    """
    A Post a User posts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField()