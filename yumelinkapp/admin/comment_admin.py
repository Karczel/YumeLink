from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Comment objects in the admin panel.
    """
    list_display = ('id', 'user', 'post', 'content', 'timestamp')
