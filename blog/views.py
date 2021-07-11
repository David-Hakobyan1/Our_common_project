from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
import random


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


def post_detail_page(request, pk):
    form = CommentForm()
    post_pk = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data.get('text'), post=post_pk, author=get_user(request))
            Comment.save(comment)
            return redirect(post_detail_page, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post_pk, 'form': form, 'comments': comments})

def Quizzes(request):
    return render(request, 'blog/Quizzes.html')


my_list = ["rock","paper","scissors"]
number1 = 0
number2 = 0
def chingachung(request):
    if request.method == 'POST':
        global my_list
        global number1
        global number2
        rands = random.randrange(len(my_list))
        player2 = my_list[rands]
        fnum = request.POST.get('fname')
        if player2 == fnum:
            pass
        if player2 == "paper" and fnum == "rock":
            number2 += 1
        if player2 == "paper" and fnum == "scissors":
            number1 += 1
        if player2 == "scissors" and fnum == "paper":
            number2 += 1
        if player2 == "scissors" and fnum == "rock":
            number1 += 1
        if player2 == "rock" and fnum == "scissors":
            number2 += 1
        if player2 == "rock" and fnum == "paper":
            number1 += 1
        return render(request,'blog/chingachung.html',{'my_list':my_list,'number1':number1,'number2':number2,'info':'ok','fnum':fnum,'player2':player2})
    return render(request,'blog/chingachung.html',{'my_list':my_list,'number1':number1,'number2':number2,'info':'start'})

def theme_selection(request):
    return render(request,'blog/theme_selection.html')

