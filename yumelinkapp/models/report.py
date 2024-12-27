from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from yumelinkapp.models import User, ReportType
from yumelinkapp.utils import BIG_TEXT


class Report(models.Model):
    """
    Reports user can send to admin.
    """
    obj_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    report_of = GenericForeignKey('content_type', 'obj_id')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    type = models.ForeignKey(ReportType, on_delete=models.CASCADE, related_name='report_type')
    content = models.TextField(max_length=BIG_TEXT, default="")
    is_justified = models.BooleanField(default=False)

    def __str__(self):
        return self.content
