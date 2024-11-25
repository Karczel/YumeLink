from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from yumelinkapp.models import ChatRoom, UserChat, Message
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


class ChatRoomView(ListView):
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


class ChatRoomDetailView(DetailView):
    model = ChatRoom
    template_name = 'yumelink/chat_room_detail.html'
    context_object_name = 'chat_room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_room = self.get_object()

        # Fetch all messages for the chat room
        messages = Message.objects.filter(chat=chat_room).order_by('timestamp')
        context['messages'] = messages

        # Get all users in the chat room from the UserChat model
        users_in_chat = UserChat.objects.filter(chat=chat_room).select_related('user')
        context['users_in_chat'] = users_in_chat

        # Pass the currently logged-in user to the template
        context['current_user'] = self.request.user

        return context


def post(self, request, *args, **kwargs):
    self.object = self.get_object()  # Get the current ChatRoom
    content = request.POST.get('message')
    if content:
        # Ensure that the user is a fully resolved instance
        if hasattr(request.user, '_wrapped'):  # Check if user is a LazyObject
            user = request.user._wrapped  # Resolve the LazyObject to the actual User instance
        else:
            user = request.user  # Directly use the user if it's already resolved

        # Create and save the message to the database
        Message.objects.create(
            chat_room=self.object,
            user=user,  # Assign the resolved user
            content=content
        )
    return redirect('yumelinkapp:chat_room_detail', pk=self.object.pk)


@login_required
@require_POST
def handle_message(request, chat_id):
    message_content = request.POST.get('message', '').strip()

    if message_content:
        # Retrieve the relevant ChatRoom based on the chat_id
        chat_room = get_object_or_404(ChatRoom, id=chat_id)

        # Create and save the message to the database
        Message.objects.create(
            user=request.user,  # The currently logged-in user
            chat=chat_room,  # The chat room this message belongs to
            content=message_content  # The actual message content
        )

    # Redirect to the chat room detail page after message is sent
    return redirect('yumelinkapp:chat_room_detail', pk=chat_id)
