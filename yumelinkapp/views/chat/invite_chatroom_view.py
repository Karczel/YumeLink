from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import ChatRoom, User, UserChat


@login_required
def invite_chatroom(request, pk, username):
    # receive post data as form and send invite notification where one approve and join
    try:
        chat = ChatRoom.objects.get(id=pk)
    except ChatRoom.DoesNotExist:
        messages.warning(request, "This chat room does not exist.")
        return redirect("yumelinkapp:chat_room")
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.warning(request, "No user with this username exists.")
        return redirect("yumelinkapp:chat_room_detail", pk=pk)
    UserChat.objects.create(user=user, chat=chat)
    return redirect("yumelinkapp:chat_room_detail", pk=pk)

