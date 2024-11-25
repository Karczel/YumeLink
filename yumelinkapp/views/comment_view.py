from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from yumelinkapp.models import Comment


class CommentView(LoginRequiredMixin,DetailView):
    model = Comment
    template_name = "yumelink/comment.html"
