from django.contrib import admin


class ReportTypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing ReportType objects in the admin panel.
    """
    list_display = ('id', 'name', 'slug', 'content')
