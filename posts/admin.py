from django.contrib import admin
from . import models
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['message','user__id','community__id']


admin.site.register(models.Post,PostAdmin)
