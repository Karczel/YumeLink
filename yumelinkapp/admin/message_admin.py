from django.contrib import admin


class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Message objects in the admin panel.
    """
    list_display = ('id', 'user', 'chat', 'content', 'timestamp')
