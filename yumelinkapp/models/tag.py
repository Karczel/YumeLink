from django.db import models


class Tag(models.Model):
    """
    A Tag that can be added to any Posts.
    """
    content = models.CharField()