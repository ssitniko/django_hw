from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.shortcuts import get_object_or_404



def hello_view(request):
    return HttpResponse('Hello everyuser')

def html_view(request):
    return render(request, 'base.html')

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})


def posts_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    return render(request, 'posts/post_detail.html', context={'post': post})

# def posts_detail_view(request):
#     posts = Post.objects.all()
#     return render(request, 'posts/post_detail.html', context={'posts': posts})