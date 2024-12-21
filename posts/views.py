from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required


def main_view(request):
    return render(request, 'base.html')

def hello_view(request):
    return HttpResponse('Hello everyuser')

def html_view(request):
    return render(request, 'base.html')

@login_required(login_url='login-view')
def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})

@login_required(login_url='login-view')
def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/post_detail.html', context={'post': post})

@login_required(login_url='login-view')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', context={"form": form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        elif form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            post = Post.objects.create(title=title, description=description, image=image)
            return HttpResponse(f'POST был создан, id: {post.id}')   