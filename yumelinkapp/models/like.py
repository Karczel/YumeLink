from django.contrib.contenttypes.models import ContentType
from django.db import models
from . import User, Post, Notification
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

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_notification()

    def create_notification(self):
        """Create notification to post owner."""
        Notification.objects.create(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(Like),
            receiver=self.post.user
        )