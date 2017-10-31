from django.views import generic
from django.shortcuts import render, redirect
from posts.models import Post


def home(request, postnav = 'newest'):

    if request.method.upper() == 'GET':
        context = {}

        if postnav == 'newest':
            posts = Post.objects.all().order_by('create_date')

        # TODO: Rank by popularlity
        elif postnav == 'popular':
            posts = Post.objects.all().order_by('create_date')

        elif postnav == 'myfeed':
            if request.user.is_authenticated:
                print(request.user.username)
                posts = Post.objects.all().filter(user__username__iexact=request.user.username).order_by('create_date')
            else:
                return redirect('accounts:login')

        context.update({
            postnav: posts,
            'user':request.user,
        })
        return render(request,'home.html',context)

    elif request.method.upper() == 'POST':
        pass

class AboutPage(generic.TemplateView):
    template_name = 'about.html'

class LoginSuccessPage(generic.TemplateView):
    template_name = 'login_success.html'

class ThanksPage(generic.TemplateView):
    template_name = 'thanks.html'
