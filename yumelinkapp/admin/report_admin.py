from django.contrib import admin


class ReportAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Report objects in the admin panel.
    """
    list_display = ('id', 'obj_id', 'content_type', 'report_of', 'reporter', 'type', 'content', 'is_justified')
