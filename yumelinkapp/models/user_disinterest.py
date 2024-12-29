from django.db import models
from . import User, Tag


class UserDisinterest(models.Model):
    """
    Keep tracks of User's disinterests in 'UserDisinterest' category.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disinterest_users')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='disinterests')

    def __str__(self):
        return f'{self.user} is disinterested in {self.tag}'
