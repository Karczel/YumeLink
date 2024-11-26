from django.views.generic import View
from django.shortcuts import render


class ReportView(View):
    template_name = 'yumelink/report.html'

    def get(self, request):
        context = {
            'title': 'Report Page',
            'options': ['Account Manage', 'Language', 'Filter content', 'More'],
        }
        return render(request, self.template_name, context)
