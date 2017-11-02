#POSTS urls
from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$',
        views.PostList.as_view(),
        name='all'),
    url(r'new/$',
        views.CreatePost.as_view(),
        name='create'),
    url(r'delete/(?P<pk>\d+)/$',
        views.delete_post,
        name='delete'),
    url(r'(?P<pk>\d+)/$',
        views.PostDetail.as_view(),
        name='single'),
]
