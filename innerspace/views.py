from django.views import generic
from django.shortcuts import render


class HomePage(generic.TemplateView):
    template_name = 'home.html'

class AboutPage(generic.TemplateView):
    template_name = 'about.html'

class LoginSuccessPage(generic.TemplateView):
    template_name = 'login_success.html'

class ThanksPage(generic.TemplateView):
    template_name = 'thanks.html'
