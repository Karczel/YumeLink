from django.db import models
from . import User, Post


class Like(models.Model):
    """
    A Like a User leaves at a Post on YumeLink.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)