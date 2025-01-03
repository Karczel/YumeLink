from django.contrib import admin


class UserDisinterestAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing UserDisinterest objects in the admin panel.
    """
    list_display = ('id', 'user', 'tag')
