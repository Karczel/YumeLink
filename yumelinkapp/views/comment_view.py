from django.views.generic import DetailView

from yumelinkapp.models import Comment


class CommentView(DetailView):
    model = Comment
    template_name = "yumelink/comment.html"
