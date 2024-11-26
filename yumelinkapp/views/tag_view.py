from django.views.generic import View
from django.shortcuts import render


class TagView(View):
    template_name = 'yumelink/tag.html'

    def get(self, request):
        context = {
            'title': 'Help Center',
            'tabs': ['FAQ', 'Contact Us'],
            'options': ['Account Management', 'Language', 'Filter Content', 'More'],
        }
        return render(request, self.template_name, context)