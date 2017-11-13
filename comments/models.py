from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
import misaka

User = get_user_model()

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=256)
    message_html = models.TextField(editable=False)
    score = models.FloatField(default=0)
    raters = models.ManyToManyField(User)
    typestr = 'Comment'

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-create_date']
        unique_together = ('user','message')
