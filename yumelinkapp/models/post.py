from django.contrib.contenttypes.models import ContentType
from django.db import models
from . import User, Follow, Notification
from yumelinkapp.utils import BIG_TEXT, SMALL_TEXT, FilterType


class Post(models.Model):
    """
    A Post a User posts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=BIG_TEXT, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    filter_content = models.CharField(
        max_length=SMALL_TEXT,
        choices=FilterType.choices(),
        default=FilterType.none,
    )

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_notification()

    def create_notification(self):
        """Create notification for followers."""
        for follow in Follow.objects.filter(user=self.user):
            if follow.notify:
                Notification.objects.create(
                    object_id=self.id,
                    content_type=ContentType.objects.get_for_model(Post),
                    receiver=follow.follower
                )

    def delete(self, *args, **kwargs):
        Notification.objects.filter(
            obj_id=self.id,
            content_type=ContentType.objects.get_for_model(Post)
        ).delete()
        super().delete(*args, **kwargs)