from .models import Post, Comment
from django import forms
from django.forms import Textarea


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['text'].widget = Textarea(attrs={'rows': 2})
