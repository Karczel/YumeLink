from django.urls import reverse
from django.views.generic import ListView
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from yumelinkapp.models import Notification, Follow, Like, Share, Message, Comment, Post, User


class NotificationView(ListView):
    model = Notification
    template_name = 'yumelink/notification.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        """
        Filters notifications for the logged-in user.
        """
        user = User.objects.get(id=self.request.user.id)
        return Notification.objects.filter(receiver=user).order_by('-timestamp')

    def get_notification_details(self, notification):
        """
        Extracts detailed information for each notification.
        """
        content = notification.notification_of
        content_type = notification.content_type
        sender = None
        url = None

        if content_type == ContentType.objects.get_for_model(Like) or \
                content_type == ContentType.objects.get_for_model(Share):
            url = reverse('yumelinkapp:post', kwargs={'pk': content.post.id})
        elif content_type == ContentType.objects.get_for_model(Comment):
            url = reverse('yumelinkapp:comment', kwargs={'post_id':content.post.id, 'pk': content.id})
        elif content_type == ContentType.objects.get_for_model(Post):
            url = reverse('yumelinkapp:post', kwargs={'pk': content.id})
        elif content_type == ContentType.objects.get_for_model(Message):
            url = reverse('yumelinkapp:chat_room_detail', kwargs={'pk': content.chat.id})
        elif content_type == ContentType.objects.get_for_model(Follow):
            url = reverse('yumelinkapp:user_profile', kwargs={'pk': content.follower.username})



        if content_type == ContentType.objects.get_for_model(Like) or \
                content_type == ContentType.objects.get_for_model(Share) or \
                content_type == ContentType.objects.get_for_model(Message) or \
                content_type == ContentType.objects.get_for_model(Comment) or \
                content_type == ContentType.objects.get_for_model(Post):
            sender = content.user
        elif content_type == ContentType.objects.get_for_model(Follow):
            sender = content.follower

        return {
            'obj': notification,
            'url': url,
            'content': content,
            'sender': sender,
        }

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the template.
        """
        context = super().get_context_data(**kwargs)
        notifications = self.get_queryset()

        # Add extra details for each notification
        context['notifications'] = [
            self.get_notification_details(notification)
            for notification in notifications
            if notification.notification_of
        ]
        context['title'] = 'Notification Page'
        context['options'] = ['Account Manage', 'Language', 'Filter content', 'Notification', 'More']
        return context
