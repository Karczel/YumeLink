from django.contrib.contenttypes.models import ContentType
from django.db import models
from . import User, Notification


class Follow(models.Model):
    """
    Keep tracks of User's relationships in 'Follow' category.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    notify = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} follows {self.follower}'

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_notification()

    def create_notification(self):
        """Create notification to user"""
        Notification.objects.create(
            object_id=self.id,
            content_type=ContentType.objects.get_for_model(Follow),
            receiver=self.user
        )