from django.contrib import admin
from yumelinkapp.models import*

from .chatroom_admin import ChatRoomAdmin
from .tag_admin import TagAdmin
from .user_admin import UserAdmin
from .post_admin import PostAdmin
from .comment_admin import CommentAdmin
from .like_admin import LikeAdmin
from .message_admin import MessageAdmin
from .post_tag_admin import PostTagAdmin
from .share_admin import ShareAdmin
from .block_admin import BlockAdmin
from .follow_admin import FollowAdmin
from .userchat_admin import UserChatAdmin
from .post_image_admin import PostImageAdmin
from .report_admin import ReportAdmin
from .notification_admin import NotificationAdmin

admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(PostTag, PostTagAdmin)
admin.site.register(Share, ShareAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(UserChat, UserChatAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(PostImage, PostImageAdmin)
admin.site.register(Notification, NotificationAdmin)
