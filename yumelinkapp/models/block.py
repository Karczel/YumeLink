from django.db import models
from . import User


class Block(models.Model):
    """
    Keep tracks of User's relationships in 'Block' category.
    """
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blockers')
    blocked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_users')

    def __str__(self):
        return f'{self.blocker} blocks {self.blocked}'
