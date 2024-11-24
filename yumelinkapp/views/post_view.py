from django.views.generic import DetailView

from yumelinkapp.models import Post, PostImage, Tag, PostTag, Like, Comment, Share, User
from yumelinkapp.utils import LikeType


class PostView(DetailView):
    """
    View for displaying Post details.
    """
    model = Post
    template_name = "yumelink/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['user'] = User.objects.get(id=self.request.user.id)
        context['post_images'] = PostImage.objects.filter(post=post)
        context['post_tags'] = PostTag.objects.filter(post=post)

        context['tags'] = Tag.objects.filter(posttag__post=post)

        context['likes'] = Like.objects.filter(post=post, type=LikeType.like.name).count()
        context['loves'] = Like.objects.filter(post=post, type=LikeType.love.name).count()
        context['shares'] = Share.objects.filter(post=post).count()
        context['comments'] = Comment.objects.filter(post=post)


        # change post to languages with auto-translate
        # + toggle off check

        return context
