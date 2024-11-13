from enum import Enum

SMALL_TEXT = 100
MID_SMALL_TEXT = 500
MID_BIG_TEXT = 2000
BIG_TEXT = 5000

UNTITLED = 'Untitled'


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