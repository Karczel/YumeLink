from django.contrib import admin


class LikeAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Like objects in the admin panel.
    """
    list_display = ('id', 'user', 'post')
