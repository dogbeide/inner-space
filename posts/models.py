from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

# from communities.models import Community

# POSTS models
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=1024)
    message_html = models.TextField(editable=False)
    score = models.FloatField(default=0.0)
    raters = models.ManyToManyField(User)
    typestr = 'Post'

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-create_date']
        unique_together = ('user','message')


#
