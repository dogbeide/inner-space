from django.contrib import admin
from . import models

# Register your models here.

class CommunityAdmin(admin.ModelAdmin):
    search_fields = ['name','description']

# class CommunityMemberInline(admin.TabularInline):
#     model = models.CommunityMember

admin.site.register(models.Community,CommunityAdmin)
