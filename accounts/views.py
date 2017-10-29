from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import Http404
from posts import models as posts_models
from . import forms

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class DashboardView(generic.ListView):
    template_name = 'accounts/dashboard.html'
    context_object_name = 'dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'Injected content'
        return context

    # def get(self,request,*args,**kwargs):
    #     pass
