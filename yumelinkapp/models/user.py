from django.contrib.auth.models import User as DjangoUser
from django.core.validators import RegexValidator
from django.db import models

from yumelinkapp.utils import SMALL_TEXT, MID_SMALL_TEXT, FilterType, LanguageType


class User(DjangoUser):
    """
    Users on Yumelink social media.
    """
    name = models.CharField(max_length=SMALL_TEXT, blank=True, null=True)
    bio = models.TextField(max_length=MID_SMALL_TEXT, blank=True, null=True)
    profile = models.ImageField(upload_to=f'{id}/', blank=True, null=True)
    header = models.ImageField(upload_to=f'{id}/', blank=True, null=True)
    color = models.CharField(
        max_length=7,
        default="#000000",
        validators=[
            RegexValidator(
                regex=r'^#([A-Fa-f0-9]{6})$',
                message='Color must be in the format #RRGGBB (e.g., #FFFFFF for white).'
            )
        ],
        help_text="Enter a color code in the format #RRGGBB."
    )
    language = models.CharField(
        max_length=SMALL_TEXT,
        choices=LanguageType.choices(),
        default=LanguageType.english,
    )
    filter_content = models.Charfield(
        max_length=SMALL_TEXT,
        choices=[FilterType.none, FilterType.mature],
        default=FilterType.none,
    )
