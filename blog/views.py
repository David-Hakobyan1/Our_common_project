from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user


class HomePageView(TemplateView):
    template_name = 'blog/home.html'


def post_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/view_post.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = get_user(request)
            Post.objects.create(title=form.cleaned_data.get('title'),
                                slug=form.cleaned_data.get('slug'),
                                body=form.cleaned_data.get('body'),
                                author=user,
                                )
            messages.success(request, f'Post successfully created!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def post_detail_page(request, pk):
    form = CommentForm()
    post_pk = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data.get('text'), post=post_pk, author=get_user(request))
            Comment.save(comment)
            return render(request, 'blog/post_detail.html', {'post': post_pk, 'form': form, 'comments': comments})

    return render(request, 'blog/post_detail.html', {'post': post_pk, 'form': form, 'comments': comments})



