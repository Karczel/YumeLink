from django.views.generic import ListView

from yumelinkapp.models import ReportType


class CommunityGuidelinesView(ListView):
    model = ReportType
    template_name = 'yumelink/community_guidelines.html'
    context_object_name = 'guidelines'

    def get_queryset(self):
        try:
            top_guideline = ReportType.objects.get(id=10)
        except ReportType.DoesNotExist:
            top_guideline = None
        guidelines = ReportType.objects.exclude(id=10).order_by('name')
        if top_guideline:
            return [top_guideline] + list(guidelines)
        return guidelines
