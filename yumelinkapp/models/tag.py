from django.db import models


class Tag(models.Model):
    """Block"""
    content = models.CharField()