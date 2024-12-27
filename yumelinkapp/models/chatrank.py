from django.db import models

from yumelinkapp.utils import SMALL_TEXT


class ChatRank(models.Model):
    """
    ChatRanks and allowed actions for Chat Roles common across all Chat Rooms
    """
    name = models.CharField(max_length=SMALL_TEXT)
    can_delete_chatroom = models.BooleanField(default=False)
    can_change_chatroom_name = models.BooleanField(default=False)

    def __str__(self):
        return self.name
