from django.contrib import admin


class ChatRoomAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing ChatRoom objects in the admin panel.
    """
    list_display = ('id', 'chat_name')
