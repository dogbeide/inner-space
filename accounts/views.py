from django.shortcuts import render
from django.contrib.auth.models import User as User_auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import Http404
from accounts import models as accounts_models
from . import forms
from posts.models import Post
import posts.models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

def user_profile(request,username):
    posts = Post.objects.all().filter(user__username__iexact=username).order_by('-create_date')
    profile_user = User.objects.get(username__iexact=username)
    context = {
        'user_posts':posts,
        'profile_user':profile_user
    }

    # Our account or another?
    if username == request.user.username:
        return render(request,'accounts/dashboard.html',context)
    else:
        return render(request,'accounts/user_profile.html',context)
