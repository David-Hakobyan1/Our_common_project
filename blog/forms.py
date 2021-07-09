from .models import Post,Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
