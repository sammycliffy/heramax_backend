from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'account_number', 'bank', 'account_name']


admin.site.register(Profile, ProfileAdmin)
