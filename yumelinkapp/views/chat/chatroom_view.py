from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from yumelinkapp.models import ChatRoom, ChatRole, User, Block


class ChatRoomView(LoginRequiredMixin,ListView):
    model = ChatRoom
    template_name = 'yumelink/chat_room.html'
    context_object_name = 'chat_room'

    def get_queryset(self):
        current_user = User.objects.get(id=self.request.user.id)
        return ChatRoom.objects.filter(chat_roles__user=current_user).order_by('chat_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        chats = self.get_queryset()

        # Add filtered chat rooms for Personal and Groups
        personal_chats = ChatRoom.objects.filter(
            id__in=ChatRole.objects.values('chat').annotate(count=Count('id')).filter(count__lte=2).values(
                'chat')
        )
        group_chats = ChatRoom.objects.filter(
            id__in=ChatRole.objects.values('chat').annotate(count=Count('id')).filter(count__gt=2).values(
                'chat')
        )

        context['personal_chats'] = chats.intersection(personal_chats)
        context['group_chats'] = chats.intersection(group_chats)

        return context

    def post(self, request, *args, **kwargs):
        data = request.POST

        # Extract parameters
        chat_name = data.get('chat_name')
        other_user_username = data.get('other_user')

        if not chat_name or not other_user_username:
            messages.error(request, "Invalid form.")
            return redirect('yumelinkapp:chat_room')

        current_user = User.objects.get(id=self.request.user.id)
        other_user = get_object_or_404(User, username=other_user_username)

        if Block.objects.filter(blocked=current_user, blocker=other_user).exists():
            messages.error(request, "This user has blocked you.")
            return redirect('yumelinkapp:chat_room')

        if Block.objects.filter(blocker=current_user, blocked=other_user).exists():
            messages.error(request, "This user has been blocked by you.")
            return redirect('yumelinkapp:chat_room')

        # Create the chat room if it doesn't exist
        # todo: accept profile for chatroom
        chat_room, created = ChatRoom.objects.get_or_create(chat_name=chat_name)

        # Create ChatRole entries
        ChatRole.objects.get_or_create(chat=chat_room, user=current_user)
        ChatRole.objects.get_or_create(chat=chat_room, user=other_user)

        return redirect('yumelinkapp:chat_room')


