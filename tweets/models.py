from django.db import models
from accounts.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Tweet(models.Model):
    handle = models.CharField(max_length=128, unique=True)
    text = models.CharField(max_length=140, unique=True)

    def __str__(self):
        self.handle

class Query(models.Model):

    user = models.ForeignKey(User, related_name='queries', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    data = JSONField()

    def __str__(self):
        return self.data

# class Tweet(models.Model):
#
#     query = models.ManyToManyField(Query, related_name='tweets')
#     data = JSONField()
#
#     def __str__(self):
#         return data
