from django.contrib.auth.models import User as DjangoUser
from django.db import models
from yumelinkapp.utils import SMALL_TEXT, MID_SMALL_TEXT


class User(DjangoUser):
    """
    Users on Yumelink social media.
    """
    name = models.CharField(max_length=SMALL_TEXT, blank=True, null=True)
    bio = models.TextField(max_length=MID_SMALL_TEXT, blank=True, null=True)

    def __str__(self):
        return self.name