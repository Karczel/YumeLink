from django.contrib.auth.decorators import login_required


@login_required
def unlove(request, post_id):
    pass