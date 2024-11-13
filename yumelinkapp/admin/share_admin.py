from django.contrib import admin


class ShareAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Share objects in the admin panel.
    """
    list_display = ('id', 'user', 'post', 'share_type')
