from django.db import models
from . import User, ChatRoom
from ..utils import SMALL_TEXT, ChatRequestActions, ChatRequestStatus


class ChatRequest(models.Model):
    """
    Keep tracks of Requests between users related to Chat Rooms.
    """
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='chatrequest_chatroom')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatrequest_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatrequest_receiver')
    action = models.CharField(max_length=SMALL_TEXT,
                              choices=ChatRequestActions.choices(),
                              default=ChatRequestActions.invite)
    status = models.CharField(max_length=SMALL_TEXT,
                              choices=ChatRequestStatus.choices(),
                              default=ChatRequestStatus.pending)

    def __str__(self):
        return f'{self.sender} {self.action}ed {self.receiver}'
