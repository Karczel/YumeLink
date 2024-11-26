from django.urls import path
from . import views


app_name = 'yumelinkapp'

urlpatterns = [
    path('chat_room/', views.ChatRoomView.as_view(), name='chat_room_list'),  # Chat rooms list
    path('chat_room/<int:pk>/', views.ChatRoomDetailView.as_view(), name='chat_room_detail'),
    path('chat/<int:chat_id>/message/', views.handle_message, name='handle_message'),
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
]