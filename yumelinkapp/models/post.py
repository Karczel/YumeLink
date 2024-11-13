from django.db import models
from . import User
from ..utils import BIG_TEXT


class Post(models.Model):
    """
    A Post a User posts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=BIG_TEXT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
