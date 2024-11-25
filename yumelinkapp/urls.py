from django.urls import path
from . import views

app_name = 'yumelinkapp'

urlpatterns = [
    path('chat_room/', views.ChatRoomView.as_view(), name='chat_room'),  # Chat rooms list
    path('chat_room/<int:pk>/', views.ChatRoomDetailView.as_view(), name='chat_room_detail'),
    path('chat_room/<int:chat_id>/message/', views.handle_message, name='handle_message'),
    path("", views.HomeView.as_view(), name="home"),
    path("post/<int:pk>", views.PostView.as_view(), name="post"),
    path("post/<int:pk>/edit", views.CreateEditPostView.as_view(), name="edit_post"),
    path("post/new", views.CreateEditPostView.as_view(), name="create_post"),
    path('chat/<int:chat_id>/message/', views.handle_message, name='handle_message'),
    path('profile/', views.ProfileView.as_view(), name='user_profile'),
    path('post/<int:post_id>/share/', views.ShareView.as_view(), name='share_post'),
]
