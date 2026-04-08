from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import Post
from interactions.models import *
from accounts.models import CustomUser
from accounts.permissions import can_edit_comment




@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()

    return redirect('detail', id=post_id)


@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            post_id=post_id,
            content=request.POST.get('content')
        )

    return redirect('detail', id=post_id)



@login_required
def toggle_follow(request, user_id):
    target = get_object_or_404(CustomUser, id=user_id)

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=target
    )

    if not created:
        follow.delete()

    return redirect('home')


@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if not can_edit_comment(request.user, comment):
        return HttpResponse("Permission Denied", status=403)

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('detail', id=comment.post.id)

    return render(request, 'edit_comment.html', {
        'comment': comment
    })


@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if not can_edit_comment(request.user, comment):
        return HttpResponse("Permission Denied", status=403)

    post_id = comment.post.id
    comment.delete()

    return redirect('detail', id=post_id)