from django.db import models
from . import User


class Follow(models.Model):
    """
    Keep tracks of User's relationships in 'Follow' category.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    notify = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} follows {self.follower}'
