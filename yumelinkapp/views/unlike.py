from django.contrib.auth.decorators import login_required


@login_required
def unlike(request, post_id):
    pass