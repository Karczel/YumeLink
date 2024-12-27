from django.db import models
from . import User, ChatRoom


class ChatRequest(models.Model):
    """
    Keep tracks of Chat Requests.
    """
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='blockers')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_users')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_users')
    action = models.CharField()
    status = models.CharField()

    def __str__(self):
        return f'{self.sender} {self.action}ed {self.receiver}'
