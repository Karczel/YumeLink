from django.contrib import admin


class PostTagAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing PostTag objects in the admin panel.
    """
    list_display = ('id', 'tag', 'post')
