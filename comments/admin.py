from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name','description']

admin.site.register(Comment,CommentAdmin)
