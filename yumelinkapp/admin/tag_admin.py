from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Tag objects in the admin panel.
    """
    list_display = ('id', 'content')
