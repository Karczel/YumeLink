from django.contrib import messages
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.edit import UpdateView
from yumelinkapp.models import Post, PostImage, User
from yumelinkapp.forms import PostTagForm, PostForm


class CreateEditPostView(UpdateView):
    """
        View for creating or editing Post details.
    """
    model = Post
    form_class = PostForm
    second_form_class = PostTagForm
    template_name = 'yumelink/create_edit_post.html'

    def get_object(self, queryset=None):
        post_id = self.kwargs.get('pk')
        if post_id:
            return get_object_or_404(Post, pk=post_id)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['post'] = self.object
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        # if 'form2' not in context:
        #     context['form2'] = PostImageFormSet(self.request.GET)
        # context['active_client'] = True

        return context

    def get(self, request, *args, **kwargs):
        super(CreateEditPostView, self).get(request, *args, **kwargs)
        form = self.form_class(instance=self.object)
        # form2 = PostImageFormSet(queryset=PostImage.objects.filter(post=self.object))
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form))

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        # if Http404: #in create view
        #     self.object = Post.object.create() / redirect to create view
        form = self.form_class(request.POST)
        # form2 = self.second_form_class(request.POST, request.FILES)

        # form2 = self.second_form_class(request.POST, request.FILES, queryset=PostImage.objects.filter(post=self.object), instance=self.object)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # post_tag = form2.save(commit=False)
            # post_image.save()
            if 'image' in request.FILES:
                image = request.FILES['image']
                post_image = PostImage.objects.create(post=post, image=image)

            # messages.info(self.request, f"Request files:{request.FILES}")
            messages.success(self.request, 'Settings saved successfully')
            return HttpResponseRedirect(reverse('yumelinkapp:post', kwargs={"pk": self.object.id}))
        else:
            messages.error(self.request, "failed to post, please try again.")

            return self.render_to_response(
                self.get_context_data(object=self.object, form=form))

    def form_valid(self, form):
        form.instance.user = User.objects.get(id=self.request.user.id)

        if form.instance.content=='':
            messages.error(self.request, 'fill content')
            return HttpResponseRedirect(reverse('yumelinkapp:edit_post', kwargs={"pk": self.object.id}))

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

