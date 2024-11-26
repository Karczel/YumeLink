from django.urls import path
from . import views


app_name = 'yumelinkapp'

urlpatterns = [
    # Chat Room URLs
    path('chat_room/', views.ChatRoomView.as_view(), name='chat_room'),  # Chat rooms list
    path('chat_room/<int:pk>/', views.ChatRoomDetailView.as_view(), name='chat_room_detail'),

    # Home and Post URLs
    path("", views.HomeView.as_view(), name="home"),
    path("post/<int:pk>", views.PostView.as_view(), name="post"),
    path("post/<int:pk>/edit", views.CreateEditPostView.as_view(), name="edit_post"),
    path("post/new", views.CreateEditPostView.as_view(), name="create_post"),
    path("post/<int:pk>/delete", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/comment/<int:pk>", views.CommentView.as_view(), name="comment"),
    path("post/<int:post_id>/comment/new", views.create_comment, name="create_comment"),
    path("post/<int:post_id>/comment/<int:pk>/delete", views.delete_comment, name="delete_comment"),
    path("post/<int:post_id>/like", views.like, name="like_post"),
    path("post/<int:post_id>/love", views.like, name="love_post"),

    # User Profile and Relationships
    path('profile/', views.ProfileView.as_view(), name='user_profile'),
    path("", views.HomeView.as_view(), name="home"),

    path('settings/', views.SettingView.as_view(), name='settings'),
    path('settings/account_manage/', views.AccountManageView.as_view(), name='account_manage'),
    path('settings/notifications/', views.NotificationView.as_view(), name='notifications'),
    path('reports/', views.ReportView.as_view(), name='reports'),
    path('settings/account_manage/login/', views.LoginView.as_view(), name='login'),
    path('settings/contact/', views.ContactView.as_view(), name='contact'),
    path('settings/tag/', views.TagView.as_view(), name='tag'),
    path('settings/account_manage/change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path("profile/relationship", views.UserRelationShipView.as_view(), name="user_relationship"),
]
