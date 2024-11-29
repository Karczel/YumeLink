from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from yumelinkapp.models import User
from yumelinkapp.utils import ReportType, BIG_TEXT, SMALL_TEXT


class Report(models.Model):
    """
    Reports user can send to admin.
    """
    obj_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    report_of = GenericForeignKey('content_type', 'obj_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    type = models.CharField(
        max_length=SMALL_TEXT,
        choices=ReportType.choices(),
        default=ReportType.other,
    )
    content = models.TextField(max_length=BIG_TEXT, default="")

    def __str__(self):
        return self.content
