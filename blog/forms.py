from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body')

    def form_valid(self, form):

        form.instance.author = self.request.user
