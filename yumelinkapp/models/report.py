from django.db import models

from yumelinkapp.models import Post, User
from yumelinkapp.utils import ReportType, BIG_TEXT, SMALL_TEXT


class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    type = models.CharField(
        max_length=SMALL_TEXT,
        choices=ReportType.choices(),
        default=ReportType.other,
    )
    content = models.TextField(max_length=BIG_TEXT, default="")

    def __str__(self):
        return self.content
