from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
# from django.views import generic
# from braces.views import SelectRelatedMixin
from django.shortcuts import render, redirect, get_object_or_404

from posts.models import Post
from .models import Comment
from .forms import CommentForm

from django.contrib.auth import get_user_model
User = get_user_model()

# COMMENTS views
# Create your views here.


@login_required
def create_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:single',pk=post.pk)

    elif request.method == 'GET':
        form = CommentForm()

    context = {}
    context.update({
        'form': form,
        'post': post,
    })
    return render(request,'comments/comment_form.html',context)

@login_required
def delete_comment(request,pk):

    comment = get_object_or_404(Comment,pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('posts:single',pk=comment.post.pk)

    else:
        return render(request,'comments/comment_confirm_delete.html',{'comment':comment})

@login_required
def rate(request, pk, rating):
    print(rating)
    comment = Comment.objects.get(pk=pk)
    request.user.rate(comment,rating)
    return redirect('home')
