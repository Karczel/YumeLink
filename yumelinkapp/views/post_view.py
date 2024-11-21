from django.views.generic import DetailView

from yumelinkapp.models import Post, PostImage


class PostView(DetailView):
    """
    View for displaying Post details.
    """
    model = Post
    template_name = "yumelink/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_images'] = PostImage.objects.filter(post=self.object)
        #change post to languages with auto-translate
        # + toggle off check

        return context
