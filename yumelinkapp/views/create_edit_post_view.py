from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from yumelinkapp.models import Post, PostImage, User, Tag, PostTag
from yumelinkapp.forms import TagForm, PostForm, TagFormSet


class CreateEditPostView(LoginRequiredMixin, UpdateView):
    """
        View for creating or editing Post details.
    """
    model = Post
    form_class = PostForm
    second_form_class = TagForm
    template_name = 'yumelink/create_edit_post.html'

    def get_object(self, queryset=None):
        post_id = self.kwargs.get('pk')
        if post_id:
            return get_object_or_404(Post, pk=post_id)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.request.user.id)
        context['post'] = self.object
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'tag_formset' not in context:
            context['tag_formset'] = TagFormSet(queryset=Tag.objects.filter(id__in=PostTag.objects.filter(post=self.object)))
        return context

    def get(self, request, *args, **kwargs):
        super(CreateEditPostView, self).get(request, *args, **kwargs)
        try:
            user = User.objects.get(id=self.request.user.id)
        except User.DoesNotExist:
            messages.warning(request, 'You have to log in as a user to edit post.')
            return redirect('yumelinkapp:home')

        if self.object.user != user:
            messages.warning(request, 'You are not the owner of this post.')
            return redirect('yumelinkapp:home')

        form = self.form_class(instance=self.object)
        tag_formset = TagFormSet(
            queryset=Tag.objects.filter(id__in=PostTag.objects.filter(post=self.object).values('tag_id'))
        )
        return self.render_to_response(self.get_context_data(
            object=self.object,
            form=form,
            tag_formset=tag_formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        post_data = request.POST.copy()
        post_data['user'] = User.objects.get(id=request.user.id)
        if self.object:
            form = self.form_class(post_data, instance=self.object)
        else:
            form = self.form_class(post_data)
        tag_formset = TagFormSet(request.POST, queryset=Tag.objects.filter(posttag__post=self.object))

        # messages.info(request, post_data)

        if form.is_valid() and tag_formset.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(id=request.user.id)
            post.save()

            PostTag.objects.filter(post=post).delete()

            for i, form in enumerate(tag_formset.forms):
                tag_name = form.cleaned_data.get('content')
                if tag_name:
                    tag, created = Tag.objects.get_or_create(content=tag_name)
                    PostTag.objects.create(post=post, tag=tag)

            if 'image' in request.FILES:
                image = request.FILES['image']
                post_image = PostImage.objects.create(post=post, image=image)

            messages.success(request, 'Post saved successfully')
            try:
                return HttpResponseRedirect(reverse('yumelinkapp:post', kwargs={"pk": self.object.id}))
            except AttributeError:
                return HttpResponseRedirect(reverse('yumelinkapp:home'))

        else:
            if form.errors:
                messages.error(request, f"form: {form.errors}")

            if tag_formset.errors:
                messages.error(request, f"Tag formset errors: {tag_formset.errors}")

            messages.error(request, "failed to post, please try again.")

            return self.render_to_response(
                self.get_context_data(object=self.object, form=form, tag_formset=tag_formset))
