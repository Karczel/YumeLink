from django.contrib import admin


class ChatRankAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing ChatRank objects in the admin panel.
    """
    list_display = ('id', 'name', 'can_delete_chatroom', 'can_change_chatroom_name')
