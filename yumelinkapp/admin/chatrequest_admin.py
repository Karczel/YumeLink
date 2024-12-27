from django.contrib import admin


class ChatRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing ChatRequest objects in the admin panel.
    """
    list_display = ('id', 'chat', 'sender', 'receiver', 'action', 'status')
