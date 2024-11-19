from django.db import models
from . import User, Post
from ..utils import LikeType, SMALL_TEXT


class Like(models.Model):
    """
    A Like a User leaves at a Post on YumeLink.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=SMALL_TEXT,
        choices=LikeType.choices(),
        default=LikeType.like,
    )

    def __str__(self):
        return f'{self.user} likes {self.post}'
