"""innerspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^about/$',views.AboutPage.as_view(),name='about'),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^comments/',include('comments.urls',namespace='comments')),
    url(r'^login-success/$',views.LoginSuccessPage.as_view(),name='login_success'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^tweets/',include('tweets.urls',namespace='tweets')),
    url(r'^(?P<postnav>[-\w]+)/$',views.home,name='home'),
    url(r'^$',views.home,name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/',
        include(debug_toolbar.urls)),
    ] + urlpatterns
