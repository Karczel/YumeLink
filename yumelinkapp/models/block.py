from django.db import models
from . import User


class Block(models.Model):
    """Block"""
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blockers')
    blocked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_users')