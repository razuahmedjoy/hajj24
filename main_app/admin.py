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
    list_display = ('id','name', 'created_by_user', 'created_at', 'updated_at')

    def created_by_user(self, obj):
        return obj.created_by.username if obj.created_by else None
    created_by_user.short_description = 'Created By'

class CameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'sn', 'tent_name')

    def tent_name(self, obj):
        return obj.tent.name if obj.tent else 'No Tent'

    tent_name.short_description = 'Tent'

class CounterHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'camera', 'sn', 'total_in', 'total_out']

    def camera_sn(self, obj):
        return obj.camera.sn if obj.camera else 'No Camera'

    camera_sn.short_description = 'Camera SN'

admin.site.register(Tent, TentAdmin)
admin.site.register(Camera, CameraAdmin)
admin.site.register(CounterHistory, CounterHistoryAdmin)
admin.site.register(CameraHeartbeat)