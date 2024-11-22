from django.contrib import admin


class NotificationAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Block objects in the admin panel.
    """
    list_display = ('object_id', 'content_type', 'notification_of', 'receiver', 'is_read', 'timestamp')
