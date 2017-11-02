from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import Http404
from django.shortcuts import render,redirect,get_object_or_404
from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

#POSTS views
# Create your views here.
class PostList(generic.ListView,SelectRelatedMixin):
    model = models.Post
    select_related = ('user','community')

class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(generic.DetailView):
    model = models.Post


class CreatePost(generic.CreateView,LoginRequiredMixin,SelectRelatedMixin):

    model = models.Post
    fields = ['message']

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class DeletePost(generic.DeleteView,LoginRequiredMixin,SelectRelatedMixin):
#
#     model = models.Post
#     select_related = ('user')
#     success_url = reverse_lazy('accounts:dashboard')
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user_id=self.request.user.id)
#
#     def delete(self,*args,**kwargs):
#         messages.success(self.request,'Post Deleted')
#         return super().delete(*args,**kwargs)

@login_required
def delete_post(request,pk):
    print('hello')
    post = get_object_or_404(models.Post,pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    else:

        return render(request,'posts/post_confirm_delete.html',{'object':post})

#
