from django.views.generic import DetailView

from yumelinkapp.models import Post, PostImage, Tag, PostTag


class PostView(DetailView):
    """
    View for displaying Post details.
    """
    model = Post
    template_name = "yumelink/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post=self.object
        context['post_images'] = PostImage.objects.filter(post=post)
        context['post_tags'] = PostTag.objects.filter(post=post)

        context['tags'] = Tag.objects.filter(posttag__post=post)

        # change post to languages with auto-translate
        # + toggle off check

        return context
