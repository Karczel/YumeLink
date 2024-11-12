from django.db import models


class ChatRoom(models.Model):
    """Block"""
    chat_name = models.CharField()