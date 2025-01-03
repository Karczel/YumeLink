# views.py
from django.http import JsonResponse
from django.views import View
from yumelinkapp.models import Share, Post, User
import json

from yumelinkapp.utils import ShareType


def track_share(request, *args, **kwargs):
    try:
        # Load the data sent via POST request
        data = json.loads(request.body)
        post_id = data.get('postId')
        share_type = ShareType.other.name
        user = User.objects.get(id=request.user.id)  # Assuming the user is logged in

        if not post_id:
            return JsonResponse({'error': 'Post ID is required'}, status=400)

        # Get the post instance based on the ID
        post = Post.objects.get(id=post_id)

        # Create a Share object to track the share
        Share.objects.create(
            user=user,
            post=post,
            share_type=share_type)

        return JsonResponse({'message': 'Share tracked successfully'}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
