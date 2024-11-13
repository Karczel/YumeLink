from django.db import models
from . import User, ChatRoom
from yumelinkapp.utils import BIG_TEXT


class Message(models.Model):
    """
    A Message a User sent in a ChatRoom.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField(max_length=BIG_TEXT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} : {self.content} in {self.chat}'
