from django.db import models
from . import User, Post


class Share(models.Model):
    """
    Share(s) of a Post by User(s).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    share_type = models.CharField()