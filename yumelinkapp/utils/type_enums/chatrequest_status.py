from enum import Enum


class ChatRequestStatus(Enum):
    pending = "Pending"
    accepted = "Accepted"
    rejected = "Rejected"

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        """Returns the choices as a list of tuples."""
        return [(status.name, status.value) for status in cls]

