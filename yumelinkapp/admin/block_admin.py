from django.contrib import admin


class BlockAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Block objects in the admin panel.
    """
    list_display = ('id', 'blocker', 'blocked')
