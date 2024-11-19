from django.db import models

from yumelinkapp.models import Post
from yumelinkapp.utils import post_image_upload_path


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=post_image_upload_path, blank=True,
                              null=True)

    def __str__(self):
        return self.image
