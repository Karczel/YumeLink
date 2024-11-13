from django.db import models

from yumelinkapp.utils import SMALL_TEXT


class Tag(models.Model):
    """
    A Tag that can be added to any Posts.
    """
    content = models.CharField(max_length=SMALL_TEXT)