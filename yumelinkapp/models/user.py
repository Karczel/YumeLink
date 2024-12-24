from django.contrib.auth.models import User as DjangoUser
from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta



from yumelinkapp.utils import SMALL_TEXT, MID_SMALL_TEXT, FilterType, LanguageType, user_profile_path, UNTITLED


class User(DjangoUser):
    """
    Users on Yumelink social media.
    """
    name = models.CharField(default=UNTITLED,max_length=SMALL_TEXT, blank=True, null=True)
    birthday = models.DateTimeField(default=datetime.now() - relativedelta(years=13))
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

    def __str__(self):
        if self.name != UNTITLED:
            return self.name
        return self.username
