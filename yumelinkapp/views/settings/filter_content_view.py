from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from yumelinkapp.forms import FilterContentForm
from yumelinkapp.models import User


class FilterContentUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = FilterContentForm
    template_name = 'yumelink/filter_content.html'
    success_url = reverse_lazy('yumelinkapp:settings')

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)