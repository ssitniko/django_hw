from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from posts.models import Post
from posts.forms import PostForm, SearchForm
from django.contrib.auth.decorators import login_required


"""
posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10, post11, post12, post13, post14,]
limit = 2
page = 4

formula:
start = (page-1) * limit = 6
end = page * limit = 9

"""



def main_view(request):
    return render(request, 'base.html')

def hello_view(request):
    return HttpResponse('Hello everyuser')

def html_view(request):
    return render(request, 'base.html')

@login_required(login_url='login-view')
def posts_list_view(request):
    if request.method == 'GET':
        limit = 4
        page = int(request.GET.get('page', 1))
        search = request.GET.get('search')
        category = request.GET.get('category')
        ordering = request.GET.get('ordering')
        form = SearchForm()
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            posts = posts.filter(category_id=category)
        if ordering:
            posts = posts.order_by(ordering)
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]
        context={'posts': posts, 'form': form, 'max_pages': range(1, max_pages + 1)}
        return render(request, 'posts/post_list.html', context=context,) 

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