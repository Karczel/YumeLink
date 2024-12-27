from django.contrib import admin


class UserInterestAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing UserInterest objects in the admin panel.
    """
    list_display = ('id', 'user', 'tag')
