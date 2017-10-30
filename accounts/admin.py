from django.contrib import admin
from . import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username','email_address']
    model = models.User

admin.site.register(models.User,UserAdmin)
