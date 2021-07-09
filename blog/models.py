from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='post', blank=True, null=True, related_name='comment_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author comment', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Comment text')
    status = models.BooleanField(verbose_name='Visibility of the post', default=False)

    def __str__(self):
        return self.text
