from django.contrib.auth.decorators import login_required


@login_required
def delete_chatroom(request):
    # receive post data as form and send invite noti where one approve and join
    pass