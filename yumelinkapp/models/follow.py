from django.db import models
from . import User


class Follow(models.Model):
    """Follow"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')