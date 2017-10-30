from django.shortcuts import render
from django.contrib.auth.models import User as User_auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import Http404
from accounts import models as accounts_models
from posts import models as posts_models
from . import forms
import posts.models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class DashboardView(generic.DetailView, LoginRequiredMixin):
    template_name = 'accounts/dashboard.html'
    context_object_name = 'dashboard'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['object'].posts.all())
        context.update({
            'test': 'Injected content',
            'user_posts': context['object'].posts.all(),
        })
        return context
