from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from yumelinkapp.models import Post, PostImage, User
from yumelinkapp.forms import PostImageFormSet


class CreateEditPostView(UpdateView):
    """
        View for creating or editing Post details.
    """
    model = Post
    template_name = 'yumelink/create_edit_post.html'
    fields = ['content', 'filter_content']

    def get_object(self, queryset=None):
        post_id = self.kwargs.get('pk')
        if post_id:
            return get_object_or_404(Post, pk=post_id)
        return None

    def form_valid(self, form):
        form.instance.user = User.objects.get(id=self.request.user.id)

        self.object = form.save()

        context = self.get_context_data()
        image_formset = context['image_formset']

        if not image_formset:
            return HttpResponseRedirect(reverse('yumelinkapp:post', kwargs={"pk": self.object.id}))

        if image_formset.is_valid():
            images = image_formset.save(commit=False)
            for image in images:
                image.post = self.object
                if image.delete_image:
                    image.delete()
                else:
                    image.save()
            for obj in image_formset.deleted_objects:
                obj.delete()

            return HttpResponseRedirect(reverse('yumelinkapp:post', kwargs={"pk": self.object.id}))
        else:
            if image_formset.errors or image_formset.management_form.errors:
                messages.info(self.request, f"Image formset errors:{image_formset.errors}")
                messages.info(self.request, f"Management form errors:{image_formset.management_form.errors}")

                messages.error(self.request, "failed to post, please try again.")

                return HttpResponseRedirect(reverse('yumelinkapp:edit_post', kwargs={"pk": self.object.id}))
        return HttpResponseRedirect(reverse('yumelinkapp:post', kwargs={"pk": self.object.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['post'] = self.object
        context['image_formset'] = PostImageFormSet(queryset=PostImage.objects.filter(post=self.object))

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
            kwargs['files'] = self.request.FILES
        else:
            kwargs['data'] = None
            kwargs['files'] = None
        return kwargs
