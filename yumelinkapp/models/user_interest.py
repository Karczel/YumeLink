from django.db import models
from . import User, Tag


class UserInterest(models.Model):
    """
    Keep tracks of User's interests in 'UserInterest' category.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interest_users')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='interests')

    def __str__(self):
        return f'{self.user} is interested in {self.tag}'
