from django.db import models
from django.contrib import auth
from django.utils.text import slugify


class User(auth.models.AbstractUser):
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return "@{}".format(self.username)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.username)
        super().save(*args,**kwargs)
