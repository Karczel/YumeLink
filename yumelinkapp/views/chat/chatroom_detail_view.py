from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView

from yumelinkapp.models import ChatRoom, Message, ChatRole, User


class ChatRoomDetailView(LoginRequiredMixin,DetailView):
    model = ChatRoom
    template_name = 'yumelink/chat_room_detail.html'
    context_object_name = 'chat_room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_room = self.get_object()

        # Fetch all messages for the chat room
        messages = Message.objects.filter(chat=chat_room).order_by('timestamp')
        context['chat_messages'] = messages

        # Get all users in the chat room from the ChatRole model
        users_in_chat = ChatRole.objects.filter(chat=chat_room).select_related('user')
        context['users_in_chat'] = users_in_chat

        # Pass the currently logged-in user to the template
        context['current_user'] = self.request.user

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the current ChatRoom
        content = request.POST.get('message')
        user=User.objects.get(id=request.user.id)
        if content:
            Message.objects.create(
                chat=self.object,
                user=user,  # Assign the resolved user
                content=content
            )
        return redirect('yumelinkapp:chat_room_detail', pk=self.object.pk)
