from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing User objects in the admin panel.
    """
    list_display = ('id', 'name', 'bio')
