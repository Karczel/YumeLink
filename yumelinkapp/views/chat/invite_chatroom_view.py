from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from yumelinkapp.forms import InviteChatForm
from yumelinkapp.models import ChatRoom, User, UserChat


class InviteChatView(LoginRequiredMixin, FormView):
    template_name = "yumelink/invite_chat.html"  # Specify your template for the form
    form_class = InviteChatForm  # Replace with an appropriate form class if needed
    success_url = reverse_lazy("yumelinkapp:chat_room")  # Default redirect URL

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        username = form.cleaned_data["username"]

        try:
            chat = ChatRoom.objects.get(id=pk)
        except ChatRoom.DoesNotExist:
            messages.warning(self.request, "This chat room does not exist.")
            return redirect(self.get_success_url())

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.warning(self.request, "No user with this username exists.")
            return redirect("yumelinkapp:chat_room_detail", pk=pk)

        if UserChat.objects.filter(user=user, chat=chat).exists():
            messages.warning(self.request, "This user is already in this chat room.")
            return redirect("yumelinkapp:chat_room_detail", pk=pk)
        # Create a UserChat instance
        UserChat.objects.create(user=user, chat=chat)

        # Redirect to chat room detail page with a success message
        messages.success(self.request, f"{user.username} has been invited to the chat room.")
        return redirect("yumelinkapp:chat_room_detail", pk=pk)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form submission.")
        return redirect(self.get_success_url())
