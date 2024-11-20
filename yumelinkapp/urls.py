from django.urls import path

from . import views

app_name = 'yumelinkapp'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("post/<int:pk>", views.PostView.as_view(), name="post"),
    path("post/<int:pk>/edit", views.CreateEditPostView.as_view(), name="edit_post"),
    path("post/new", views.CreateEditPostView.as_view(), name="create_post")
]