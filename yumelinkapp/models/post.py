from django.db import models


class Post(models.Model):
    """Block"""
    post_id = models.IntegerField