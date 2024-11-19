from django.db import models
from . import User
from yumelinkapp.utils import BIG_TEXT, SMALL_TEXT, FilterType


class Post(models.Model):
    """
    A Post a User posts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=BIG_TEXT)
    timestamp = models.DateTimeField(auto_now_add=True)
    filter_content = models.Charfield(
        max_length=SMALL_TEXT,
        choices=FilterType.choices(),
        default=FilterType.none,
    )

    def __str__(self):
        return self.content
