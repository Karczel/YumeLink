from django.db import models

from yumelinkapp.models import Post


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'{post.user.id}/post/{post.id}/', blank=True, null=True)

    def __str__(self):
        return self.image
