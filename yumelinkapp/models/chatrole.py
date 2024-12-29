from django.db import models
from . import User, ChatRoom, ChatRank


class ChatRole(models.Model):
    """
    Chat Roles of Users in Chat Rooms.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_roles')
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='chat_roles')
    rank = models.ForeignKey(ChatRank, on_delete=models.CASCADE, related_name='chat_roles')

    def __str__(self):
        return f'{self.user} in {self.chat} as {self.rank}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'chat'], name='unique_user_chat_role')
        ]