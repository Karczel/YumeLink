from django.db import models

from yumelinkapp.utils import SMALL_TEXT, UNTITLED, chatroom_profile_path


class ChatRoom(models.Model):
    """
    ChatRooms where Users can talk with each other.
    """
    chat_name = models.CharField(max_length=SMALL_TEXT, default=UNTITLED)
    profile = models.ImageField(upload_to=chatroom_profile_path, blank=True, null=True)

    def __str__(self):
        return self.chat_name
