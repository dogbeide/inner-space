from django.contrib import admin
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username','email_address']
