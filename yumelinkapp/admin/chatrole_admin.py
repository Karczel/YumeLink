from django.contrib import admin


class ChatRoleAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing ChatRole objects in the admin panel.
    """
    list_display = ('id', 'user', 'chat', 'rank')
