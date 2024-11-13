from django.db import models
from . import User, Post
from ..utils import MID_SMALL_TEXT


class Comment(models.Model):
    """
    A Comment a User leaves at a Post on YumeLink.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=MID_SMALL_TEXT)
    timestamp = models.DateTimeField(auto_now_add=True)
