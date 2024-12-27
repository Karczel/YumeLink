from django.db import models
from django.utils.text import slugify

from yumelinkapp.utils import SMALL_TEXT, BIG_TEXT


class ReportType(models.Model):
    """
    Keep tracks of Report Types or Community Guidelines.
    """
    name = models.CharField(max_length=SMALL_TEXT)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=BIG_TEXT)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self.__class__.objects.filter(id=self.id).first().name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
