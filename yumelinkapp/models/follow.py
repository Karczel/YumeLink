from django.db import models
from . import User


class Follow(models.Model):
    """
    Keep tracks of User's relationships in 'Follow' category.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')