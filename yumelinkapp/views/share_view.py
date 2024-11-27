from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from yumelinkapp.models import Post, Share, User
from ..forms import ShareForm


class ShareView(LoginRequiredMixin,View):
    """
    Handles sharing a post. The share action could be via a link, reblog, or any other share type.
    """

    template_name = "yumelink/share_post.html"  # Ensure this is the correct template path

    def get(self, request, post_id):
        # Get the post that the user wants to share
        post = get_object_or_404(Post, id=post_id)

        # Create a form instance
        form = ShareForm()

        context = {
            'post': post,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, post_id):
        # Get the post that the user wants to share
        post = get_object_or_404(Post, id=post_id)
        user = User.objects.get(id=request.user.id)
        # Handle form submission and create the share object
        form = ShareForm(request.POST)

        if form.is_valid():
            share_type = form.cleaned_data['share_type']  # Get the selected share type

            # Create a new share entry
            share = Share.objects.create(
                user=user,
                post=post,
                share_type=share_type
            )

            # Optionally, create a notification if this is a reblog
            if share_type == 'Reblog':  # If reblog, notify the original poster
                share.create_notification()  # Ensure create_notification() is defined

            # Show a success message to the user
            messages.success(request, f'Post shared successfully as a {share_type}!')

            # Redirect to the post detail page (ensure 'post_detail' is the correct URL name)
            return redirect('yumelinkapp:post', pk=post.id)

        else:
            # Handle invalid form submission (e.g., show an error message)
            messages.error(request, 'There was an issue sharing the post. Please try again.')
            return render(request, self.template_name, {
                'post': post,
                'form': form,
            })
