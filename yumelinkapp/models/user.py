from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(DjangoUser):
    """Users on Yumelink social media."""
