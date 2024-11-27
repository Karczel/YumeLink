from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView
from yumelinkapp.models import ChatRoom, UserChat


class ChatRoomView(LoginRequiredMixin,ListView):
    model = ChatRoom
    template_name = 'yumelink/chat_room.html'
    context_object_name = 'chat_room'

    def get_queryset(self):
        # Example: Only return active chat rooms
        return ChatRoom.objects.all().order_by('chat_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add filtered chat rooms for Personal and Groups
        context['personal_chats'] = ChatRoom.objects.filter(
            id__in=UserChat.objects.values('chat').annotate(count=Count('id')).filter(count__lte=2).values(
                'chat')
        )
        context['group_chats'] = ChatRoom.objects.filter(
            id__in=UserChat.objects.values('chat').annotate(count=Count('id')).filter(count__gt=2).values(
                'chat')
        )
        return context


