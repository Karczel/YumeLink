from django.contrib.contenttypes.models import ContentType
from django.db import models
from . import User, ChatRoom, ChatRole, Notification
from yumelinkapp.utils import BIG_TEXT


class Message(models.Model):
    """
    A Message a User sent in a ChatRoom.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField(max_length=BIG_TEXT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.create_notification()

    def create_notification(self):
        """Create notification to everyone in chat."""
        for receiver in ChatRole.objects.filter(chat=self.chat):
            if receiver.user != self.user:
                Notification.objects.create(
                    object_id=self.id,
                    content_type=ContentType.objects.get_for_model(Message),
                    receiver=receiver.user
                )

    def delete(self, *args, **kwargs):
        Notification.objects.filter(
            obj_id=self.id,
            content_type=ContentType.objects.get_for_model(Message)
        ).delete()
        super().delete(*args, **kwargs)