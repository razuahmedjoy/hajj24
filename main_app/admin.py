# admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

User = get_user_model()

# # Unregister the User model if it is already registered
# try:
#     admin.site.unregister(User)
# except admin.sites.NotRegistered:
#     pass

# class CustomUserAdmin(UserAdmin):
#     list_display = ('id', 'username', 'email', 'is_staff', 'is_active')

# # Register the User model with the custom admin class
# admin.site.register(User, CustomUserAdmin)

class TentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by_user', 'created_at', 'updated_at')

    def created_by_user(self, obj):
        return obj.created_by.username if obj.created_by else None
    created_by_user.short_description = 'Created By'

admin.site.register(Tent, TentAdmin)
