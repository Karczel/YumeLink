from django.contrib import admin


class ReportAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Report objects in the admin panel.
    """
    list_display = ('id', 'post', 'user', 'reporter', 'type', 'content')
