from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from yumelinkapp.models import Post, PostImage


class HomeView(TemplateView):
    template_name = 'yumelink/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_with_images'] = [
            {
                'post': post,
                'post_images': PostImage.objects.filter(post=post)
            }
            for post in Post.objects.all().order_by('-timestamp')
        ]
        return context

    def post(self, request, *args, **kwargs):
        # add create post as request post/use url create_post
        return HttpResponse(self.get(request))
