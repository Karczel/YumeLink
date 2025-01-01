SMALL_TEXT = 100
MID_SMALL_TEXT = 500
MID_BIG_TEXT = 2000
BIG_TEXT = 5000

UNTITLED = 'Untitled'


def user_profile_path(instance, filename):
    return f'users/{instance.id}/{filename}'


def chatroom_profile_path(instance, filename):
    return f'chatrooms/{instance.id}/{filename}'


def post_image_upload_path(instance, filename):
    if instance.post and instance.post.user:
        return f'users/{instance.post.user.id}/post/{instance.post.id}/{filename}'
    return f'unknown/post/{filename}'
