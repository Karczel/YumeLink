from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Post objects in the admin panel.
    """
    list_display = ('id', 'user', 'content', 'timestamp')
