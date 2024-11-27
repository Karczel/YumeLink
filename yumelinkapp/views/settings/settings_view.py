from django.views.generic import View
from django.shortcuts import render
from yumelinkapp.models import user


class SettingView(View):
    model = user
    template_name = 'yumelink/setting_t.html'
    context_object_name = 'setting'

    def get(self, request):
        context = {
            'title': 'Settings Page',
            'options': ['Account Manage', 'Language', 'Filter content', 'Notification', 'contact']
        }
        return render(request, self.template_name, context)


class Account_manage_view:
    def account_manage_view(request):
        return render(request, 'settings/account_manage_setting.html')