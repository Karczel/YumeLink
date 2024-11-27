from django.views.generic import TemplateView


class AccountManageView(TemplateView):
    template_name = 'yumelink/account_manage_setting.html'
