from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from yumelinkapp.models import Post, PostImage, User, Block


class HomeView(TemplateView):
    template_name = 'yumelink/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            current_user = User.objects.get(id=self.request.user.id)
            blocking_users = Block.objects.filter(blocked=current_user).values_list('blocker', flat=True)
            blocked_users = Block.objects.filter(blocker=current_user).values_list('blocked', flat=True)
            excluded_users = set(blocking_users) | set(blocked_users)

            posts = Post.objects.all().exclude(user__id__in=excluded_users).order_by('-timestamp')

        except User.DoesNotExist:
            posts = Post.objects.all().order_by('-timestamp')


        context['posts_with_images'] = [
            {
                'post': post,
                'post_images': PostImage.objects.filter(post=post)
            }
            for post in posts
        ]
        return context

    def post(self, request, *args, **kwargs):
        # add create post as request post/use url create_post
        return HttpResponse(self.get(request))
