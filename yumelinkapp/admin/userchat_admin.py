from django.contrib import admin


class UserChatAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing UserChat objects in the admin panel.
    """
    list_display = ('id', 'user', 'chat')
