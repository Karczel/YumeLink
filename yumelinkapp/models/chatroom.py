from django.db import models

from yumelinkapp.utils import SMALL_TEXT, UNTITLED


class ChatRoom(models.Model):
    """
    ChatRooms where Users can talk with each other.
    """
    chat_name = models.CharField(max_length=SMALL_TEXT, default=UNTITLED)
