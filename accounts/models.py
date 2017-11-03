from django.db import models
from django.contrib import auth
from django.utils.text import slugify
import random

from innerspace import sitestats
from innerspace.sitestats import BASE_RATING_SHIFT


class User(auth.models.AbstractUser):
    slug = models.SlugField(allow_unicode=True,unique=True)
    rep = models.FloatField(default=5.00)
    power = models.FloatField(default=1.0)
    scale = models.FloatField(default=1.0)
    rank = models.PositiveIntegerField(default=random.randrange(1000000000,2000000000))
    typestr = 'User'


    def __str__(self):
        return "@{}".format(self.username)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.username)
        super().save(*args,**kwargs)

    '''
    Recalculate stats
    '''
    def respec(self):
        self.power = sitestats.power(self.rep)
        self.scale = sitestats.scale(self.rep)
        self.save()

    def rate(self,item,rating):
        # User rates a post
        if item.typestr == 'Post' or item.typestr == 'Comment':
            # Check if voted or own post
            if self in item.raters.all() or self is item.user:
                return

            # Post/Comment rating change
            if rating == '+':
                item.score += self.power
            elif rating == '-':
                item.score -= self.power
            item.raters.add(self)
            item.save()

            # Recipient User rating change,
            # Positive gives normal, negative subtracts half (promotes growth)
            shift = 0
            if rating == '+':
                shift = BASE_RATING_SHIFT*item.user.scale*self.power
            elif rating == '-':
                shift = (BASE_RATING_SHIFT/2)*item.user.scale*self.power*(-1)
            item.user.rep += shift
            item.user.respec()


        # TODO: User rates another User's profile
        elif item.typestr == 'User':
            print('User rating not yet implemented (TODO:)')

        # User gains small amount of rating for activity
        self.rep += (BASE_RATING_SHIFT/10)*self.scale
        self.respec()
