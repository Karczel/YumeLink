from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from yumelinkapp.models import Report, User
from yumelinkapp.forms import ReportForm


class ReportView(LoginRequiredMixin, CreateView):
    model = Report
    template_name = 'yumelink/report.html'
    form_class = ReportForm
    success_url = reverse_lazy('yumelinkapp:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Extract `content_type` (model name) and `obj_id` from URL
        obj_id = self.kwargs.get('obj_id')
        content_type_name = self.kwargs.get('content_type').lower()

        # Resolve ContentType and object being reported
        content_type = get_object_or_404(ContentType, model=content_type_name)
        obj = get_object_or_404(content_type.model_class(), id=obj_id)

        context['object'] = obj  # Pass object to the template
        context['content_type'] = content_type  # Pass content type if needed
        return context

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        # Extract `content_type` (model name) and `obj_id` from URL
        obj_id = self.kwargs.get('obj_id')
        content_type_name = self.kwargs.get('content_type').lower()

        # Resolve ContentType and object being reported
        content_type = get_object_or_404(ContentType, model=content_type_name)
        obj = get_object_or_404(content_type.model_class(), id=obj_id)

        # Create the report
        report = form.save(commit=False)  # Don't commit to DB just yet
        report.obj_id = obj.id
        report.content_type = content_type
        report.user = user  # Assign the logged-in user
        report.save()

        messages.success(self.request, "Your report has been submitted successfully.")
        return redirect(self.success_url)
