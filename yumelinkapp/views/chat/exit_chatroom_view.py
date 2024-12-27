from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from yumelinkapp.models import ChatRoom, User, ChatRole


@login_required
def exit_chatroom(request, pk):
    # receive post data as form and send invite noti where one approve and join
    try:
        chat = ChatRoom.objects.get(id=pk)
    except ChatRoom.DoesNotExist:
        messages.warning(request, "This chat room does not exist.")
        return redirect("yumelinkapp:chat_room")
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        messages.warning(request, "You have to log in as a user to exit chatroom.")
        return redirect("yumelinkapp:chat_room_detail", pk=pk)
    try:
        chatrole = ChatRole.objects.filter(user=user, chat=chat).first()
    except ChatRole.DoesNotExist:
        messages.warning(request, "You are not in this room.")
        return redirect("yumelinkapp:chat_room_detail", pk=pk)
    chatrole.delete()
    messages.success(request, f"You have left {chat.chat_name} room.")
    return redirect("yumelinkapp:chat_room")

