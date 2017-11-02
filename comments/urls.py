from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^new/(?P<pk>\d+)/$',
        views.create_comment,
        name='create'),
    url(r'^delete/(?P<pk>\d+)/$',
            views.delete_comment,
            name='delete'),
]
