from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from yumelinkapp.models import Post, PostImage
from yumelinkapp.forms import PostImageFormSet


class CreateEditPostView(UpdateView):
    """
        View for creating or editing Post details.
    """
    model = Post
    template_name = 'yumelink/create_edit_post.html'
    fields = ['content', 'filter_content']
    success_url = reverse_lazy('yumelinkapp:home')

    def get_object(self, queryset=None):
        post_id = self.kwargs.get('pk')
        if post_id:
            return get_object_or_404(Post, pk=post_id)
        return None

    def form_valid(self, form):
        if not self.get_object():
            form.instance.author = self.request.user
        post = form.save()

        context = self.get_context_data()
        image_formset = context['image_formset']
        if image_formset.is_valid():
            post = form.save()
            images = image_formset.save(commit=False)
            for image in images:
                image.post = post
                image.save()
            for obj in image_formset.deleted_objects:
                obj.delete()

            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['post'] = self.object
        if self.request.method == 'POST':
            context['image_formset'] = PostImageFormSet(self.request.POST, self.request.FILES,
                                                        queryset=PostImage.objects.filter(post=self.object))
        else:
            context['image_formset'] = PostImageFormSet(queryset=PostImage.objects.filter(post=self.object))

        return context
