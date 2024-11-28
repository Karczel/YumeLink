from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView
from yumelinkapp.models import ChatRoom, UserChat, User


class ChatRoomView(LoginRequiredMixin,ListView):
    model = ChatRoom
    template_name = 'yumelink/chat_room.html'
    context_object_name = 'chat_room'

    def get_queryset(self):
        current_user = User.objects.get(id=self.request.user.id)
        return ChatRoom.objects.filter(userchat__user=current_user).order_by('chat_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        chats = self.get_queryset()

        # Add filtered chat rooms for Personal and Groups
        personal_chats = ChatRoom.objects.filter(
            id__in=UserChat.objects.values('chat').annotate(count=Count('id')).filter(count__lte=2).values(
                'chat')
        )
        group_chats = ChatRoom.objects.filter(
            id__in=UserChat.objects.values('chat').annotate(count=Count('id')).filter(count__gt=2).values(
                'chat')
        )

        context['personal_chats'] = chats.intersection(personal_chats)
        context['group_chats'] = chats.intersection(group_chats)

        return context


