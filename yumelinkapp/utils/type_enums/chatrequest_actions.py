from enum import Enum


class ChatRequestActions(Enum):
    invite = "Invite"
    kick = "Kick"
    ban = "Ban"

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        """Returns the choices as a list of tuples."""
        return [(status.name, status.value) for status in cls]

