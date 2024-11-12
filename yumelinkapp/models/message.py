from django.db import models
from . import User, ChatRoom


class Message(models.Model):
    """
    A Message a User sent in a ChatRoom.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField()
