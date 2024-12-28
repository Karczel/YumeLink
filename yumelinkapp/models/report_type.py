from django.db import models
from django.utils.text import slugify

from yumelinkapp.utils import SMALL_TEXT, BIG_TEXT


class ReportType(models.Model):
    """
    Keep tracks of Report Types or Community Guidelines.
    """
    name = models.CharField(max_length=SMALL_TEXT)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(max_length=BIG_TEXT)

    def save(self, *args, **kwargs):
        if not self.slug or (self.id and self.name != self.__class__.objects.get(id=self.id).name):
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while self.__class__.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
