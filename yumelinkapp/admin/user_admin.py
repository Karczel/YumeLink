from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing User objects in the admin panel.
    """
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'name', 'birthday', 'age', 'bio', 'profile', 'header', 'color', 'language', 'filter_content')
