from django.db import models


class ChatRoom(models.Model):
    """
    ChatRooms where Users can talk with each other.
    """
    chat_name = models.CharField()