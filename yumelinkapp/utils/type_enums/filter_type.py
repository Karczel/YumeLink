from enum import Enum


class FilterType(Enum):
    none = "None"
    mature = "Mature"
    violent = "Violent"
    nudity = "Nudity"
    suggestive = "Sexually Suggestive Themes"
    drug = "Substance abuse"

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        """Returns the choices as a list of tuples."""
        return [(status.name, status.value) for status in cls]

