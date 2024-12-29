from datetime import date

from django.contrib.auth.models import User as DjangoUser
from django.core.validators import RegexValidator
from django.db import models


from yumelinkapp.utils import SMALL_TEXT, MID_SMALL_TEXT, FilterType, LanguageType, user_profile_path, UNTITLED


class User(DjangoUser):
    """
    Users on Yumelink social media.
    """
    name = models.CharField(default=UNTITLED, max_length=SMALL_TEXT, blank=True, null=True)
    birthday = models.DateField(blank=False, null=False)
    bio = models.TextField(max_length=MID_SMALL_TEXT, blank=True, null=True)
    profile = models.ImageField(upload_to=user_profile_path, blank=True, null=True)
    header = models.ImageField(upload_to=user_profile_path, blank=True, null=True)
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
        default=LanguageType.ENG,
    )
    filter_content = models.CharField(
        max_length=SMALL_TEXT,
        choices=[
            (FilterType.none.name, FilterType.none.value),
            (FilterType.mature.name, FilterType.mature.value)
        ],
        default=FilterType.none,
    )

    def age(self):
        today = date.today()
        age = today.year - self.birthday.year
        if today.month < self.birthday.month or (today.month == self.birthday.month and today.day < self.birthday.day):
            age -= 1
        return age

    def __str__(self):
        if self.name != UNTITLED:
            return self.name
        return self.username
