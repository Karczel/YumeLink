from django.contrib import admin


class FollowAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Follow objects in the admin panel.
    """
    list_display = ('id', 'user', 'follower')
