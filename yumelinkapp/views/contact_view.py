from django.views.generic import View
from django.shortcuts import render


class ContactView(View):
    template_name = 'yumelink/contact.html'

    def get(self, request):
        context = {
            'title': 'Help Center',
            'tabs': ['FAQ', 'Contact Us'],
            'options': ['Account Manage', 'Language', 'Filter Content', 'More'],
        }
        return render(request, self.template_name, context)