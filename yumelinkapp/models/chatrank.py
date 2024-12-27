from django.db import models
from . import User


class ChatRank(models.Model):
    """
    ChatRanks and allowed actions for Chat Roles common across all Chat Rooms
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_rank_label')
    delete_chatroom = models.BooleanField()
    change_chatroom_name = models.BooleanField()

    def __str__(self):
        return f'{self.blocker} blocks {self.blocked}'
