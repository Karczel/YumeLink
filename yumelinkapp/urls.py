from django.urls import path
from . import views

app_name = 'yumelinkapp'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('chat_room/', views.ChatRoomView.as_view(), name='chat_room_list'),  # Chat rooms list
    path('chat_room/<int:pk>/', views.ChatRoomDetailView.as_view(), name='chat_room_detail'),
    path("post/<int:pk>", views.PostView.as_view(), name="post"),
    path("post/<int:pk>/edit", views.CreateEditPostView.as_view(), name="edit_post"),
    path("post/new", views.CreateEditPostView.as_view(), name="create_post"),
    path("post/<int:pk>/delete", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/comment/<int:pk>", views.CommentView.as_view(), name="comment"),
    path("post/<int:post_id>/comment/new", views.create_comment, name="create_comment"),
    path("post/<int:post_id>/comment/<int:pk>/delete", views.delete_comment, name="delete_comment"),
    path("post/<int:post_id>/like", views.like, name="like_post"),
    path("post/<int:post_id>/love", views.like, name="love_post"),
    path('chat_room/', views.ChatRoomView.as_view(), name='chat_room_list'),  # Chat rooms list
    path('chat_room/<int:pk>/', views.ChatRoomDetailView.as_view(), name='chat_room_detail'),
    path('profile/', views.ProfileView.as_view(), name='user_profile'),
    path("profile/relationship", views.UserRelationShipView.as_view(), name="user_relationship"),
]
