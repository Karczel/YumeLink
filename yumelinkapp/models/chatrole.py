from django.db import models
from . import User, ChatRoom, ChatRank


class ChatRole(models.Model):
    """
    Chat Roles of Users in Chat Rooms.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    rank = models.ForeignKey(ChatRank, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user} in chatroom {self.chat}'
