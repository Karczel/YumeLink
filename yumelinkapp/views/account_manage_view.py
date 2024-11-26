from django.views.generic import View
from django.shortcuts import render


class AccountManageView(View):
    template_name = 'yumelink/account_manage_setting.html'

    def get(self, request):
        context = {
            'title': 'Account Manage Page',
            'options': ['Account Manage', 'Language', 'Filter content', 'Notification', 'More'],
        }
        return render(request, self.template_name, context)
