from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from yumelinkapp.models import Post, PostImage, User, Block


class HomeView(ListView):
    model = Post
    template_name = 'yumelink/home.html'
    context_object_name = 'posts_with_images'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')

        try:
            current_user = User.objects.get(id=self.request.user.id)
            blocking_users = Block.objects.filter(blocked=current_user).values_list('blocker', flat=True)
            blocked_users = Block.objects.filter(blocker=current_user).values_list('blocked', flat=True)
            excluded_users = set(blocking_users) | set(blocked_users)

            if search_query:
                # Filter posts by content if a search query is provided
                queryset = Post.objects.filter(
                    Q(content__icontains=search_query) |  # Filter by content
                    Q(posttag__tag__content__icontains=search_query) |  # Filter by tag name (assuming you have a Many-to-Many relation 'tags')
                    Q(user__username__icontains=search_query) |  # Filter by username
                    Q(user__name__icontains=search_query)
                ).exclude(
                    user__id__in=excluded_users).order_by('-timestamp')
            else:
                queryset = Post.objects.all().exclude(user__id__in=excluded_users).order_by('-timestamp')

        except User.DoesNotExist:
            queryset = Post.objects.all().order_by('-timestamp')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')
        context['search_query'] = search_query

        context['posts_with_images'] = [
            {
                'post': post,
                'post_images': PostImage.objects.filter(post=post)
            }
            for post in self.get_queryset()
        ]
        return context

