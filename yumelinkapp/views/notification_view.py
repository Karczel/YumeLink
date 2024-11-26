from django.views.generic import View
from django.shortcuts import render
from yumelinkapp.models import Notification, User


class NotificationView(View):
    template_name = 'yumelink/notification.html'

    def get(self, request):
        notifications = Notification.objects.select_related('receiver', 'content_type').all()
        context = {
            'title': 'Notification Page',
            'options': ['Account Manage', 'Language', 'Filter content', 'Notification', 'More'],
            'notifications': notifications,
        }
        return render(request, self.template_name, context)