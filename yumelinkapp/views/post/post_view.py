from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView

from yumelinkapp.models import Post, PostImage, Tag, PostTag, Like, Comment, Share, User, Block
from yumelinkapp.utils import LikeType, translate_text, query


class PostView(LoginRequiredMixin, DetailView):
    """
    View for displaying Post details.
    """
    model = Post
    template_name = "yumelink/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        try:
            user = User.objects.get(id=self.request.user.id)
            context['user'] = user

            context['language'] = user.get_language_display()
        except User.DoesNotExist:
            user = None
        context['content'] = self.object.content
        context['translated_content'] = translate_text(self.object.content, user.language)

        context['post_images'] = PostImage.objects.filter(post=post)
        image_captions = []
        for i, image in enumerate(context['post_images']):
            try:
                caption = query(image.image.url)  # Call the query function to get the caption
                image_captions.append((i + 1, caption))  # Add the result if successful
            except Exception as e:
                # Handle the exception (e.g., log it, append a default caption, or continue)
                image_captions.append((i + 1, [{"generated_text": "Failed to caption image(s)"}]))
                messages.error(self.request, f"Error processing image {image.image.url}: {e}")

        context['image_captions'] = image_captions

        context['post_tags'] = PostTag.objects.filter(post=post)

        context['tags'] = Tag.objects.filter(posttag__post=post)

        context['has_liked'] = Like.objects.filter(user=user, post=post, type=LikeType.like.name).exists()
        context['has_loved'] = Like.objects.filter(user=user, post=post, type=LikeType.love.name).exists()

        context['likes'] = Like.objects.filter(post=post, type=LikeType.like.name).count()
        context['loves'] = Like.objects.filter(post=post, type=LikeType.love.name).count()
        context['shares'] = Share.objects.filter(post=post).count()
        context['comments'] = [
            {
                'comment': comment,
                'owns': user == comment.user
            }
            for comment in Comment.objects.filter(post=post).order_by('-timestamp')
        ]

        # change post to languages with auto-translate
        # + toggle off check

        return context

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post_owner = post.user
        current_user = User.objects.get(id=request.user.id)

        # Check if the current user is blocked by the post owner
        is_blocked = Block.objects.filter(blocker=post_owner, blocked=current_user).exists()

        if is_blocked:
            messages.warning(request, "You are blocked by this user")
            # Redirect to a "blocked" page or another relevant page
            return redirect('yumelinkapp:home')

        return super().get(request, *args, **kwargs)