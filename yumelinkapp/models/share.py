from django.contrib.contenttypes.models import ContentType
from django.db import models
from . import User, Post, Notification
from yumelinkapp.utils import SMALL_TEXT, ShareType


class Share(models.Model):
    """
    Share(s) of a Post by User(s).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    share_type = models.CharField(max_length=SMALL_TEXT,
                                  choices=ShareType.choices(),
                                  default=ShareType.link)

    def __str__(self):
        return f'{self.user} shared {self.post} with {self.share_type}'

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_notification()

    def create_notification(self):
        """Create notification to post owner (when re-blogged)."""
        if self.share_type == ShareType.reblog.name:
            Notification.objects.create(
                object_id=self.id,
                content_type=ContentType.objects.get_for_model(Share),
                receiver=self.post.user
            )

    def delete(self, *args, **kwargs):
        Notification.objects.filter(
            obj_id=self.id,
            content_type=ContentType.objects.get_for_model(Share)
        ).delete()
        super().delete(*args, **kwargs)