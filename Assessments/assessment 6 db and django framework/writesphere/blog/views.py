from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from accounts.permissions import can_edit_post, can_delete_post, can_edit_comment
from accounts.decorators import create_permission_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from interactions.models import *

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

@login_required
def detail(request, id):
    post = get_object_or_404(Post, id=id)

    can_edit = can_edit_post(request.user, post)


    is_following = False
    is_liked = False

    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=post.author
        ).exists()

        is_liked = Like.objects.filter(
            user=request.user,
            post=post
        ).exists()

    comments = Comment.objects.filter(post=post)
    comments = Comment.objects.filter(post=post)

    for comment in comments:
        comment.can_edit = can_edit_comment(request.user, comment)

    return render(request, 'detail.html', {
        'post': post,
        'is_following': is_following,
        'is_liked': is_liked,
        'comments': comments,
        'can_edit':can_edit,
    })

@login_required
@create_permission_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        cover_image = request.FILES.get('cover_image')
        
        Post.objects.create(title=title, content=content,author = request.user,cover_image = cover_image)
        return redirect('home')

    return render(request, 'create.html')

@login_required
def update(request, id):
    post = get_object_or_404(Post, id=id)

    if not can_edit_post(request.user, post):
        return HttpResponse("Permission Denied", status=403)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        if request.FILES.get('cover_image'):
            post.cover_image = request.FILES.get('cover_image')
        post.save()
        return redirect('detail', id=id)

    return render(request, 'update.html', {'post': post})

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)

    if not can_delete_post(request.user, post):
        return HttpResponse("Permission Denied", status=403)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'delete.html', {'post': post})

