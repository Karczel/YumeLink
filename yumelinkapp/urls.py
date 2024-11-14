from django.urls import path

from . import views

app_name = 'yumelinkapp'

urlpatterns = [
    path("example/", views.example, name='example')
]