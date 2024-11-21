from django.forms import modelformset_factory, BaseModelFormSet


class BasePostImageFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        self.post_instance = kwargs.pop('post', None)
        super(BasePostImageFormSet, self).__init__(*args, **kwargs)

        # Pass 'post_instance' to each form in the formset
        for form in self.forms:
            form.instance.post = self.post_instance
