from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

from communities.models import Community

# POSTS models
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts')
    create_date = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=4096)
    message_html = models.TextField(editable=False)
    community = models.ForeignKey(Community,related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,
                                              'pk':self.pk})
    class Meta:
        ordering = ['-create_date']
        unique_together = ('user','message')

#
