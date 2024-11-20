from django.contrib import admin


class PostImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing PostImage objects in the admin panel.
    """
    list_display = ('id', 'post', 'image')
