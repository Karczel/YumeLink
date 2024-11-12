from enum import Enum


class ShareType(Enum):
    link = 'Link'
    line = 'Line'
    facebook = 'Facebook'
    tumblr = 'tumblr'

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        """Returns the choices as a list of tuples."""
        return [(status.name, status.value) for status in cls]