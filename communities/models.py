from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse

# COMMUNITIES models
# Create your models here.
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


class Community(models.Model):
    name = models.CharField(max_length=256,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    # members = models.ManyToManyField(User,through='CommunityMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('communities:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


# class CommunityMember(models.Model):
#     community = models.ForeignKey(Community,related_name='Members')
#     user = models.ForeignKey(User,related_name='user_communities')
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         unique_together = ('community','user')


#
