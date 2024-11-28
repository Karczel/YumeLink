from django.views.generic import TemplateView


class AboutUsView(TemplateView):
    template_name = 'yumelink/about_us.html'
