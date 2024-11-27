from django.contrib.contenttypes.models import ContentType
from django.db import models
from . import User, Post, Notification
from ..utils import MID_SMALL_TEXT


class Comment(models.Model):
    """
    A Comment a User leaves at a Post on YumeLink.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=MID_SMALL_TEXT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_notification()

    def create_notification(self):
        """Create notification to post owner."""
        Notification.objects.create(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(Comment),
            receiver=self.post.user
        )
