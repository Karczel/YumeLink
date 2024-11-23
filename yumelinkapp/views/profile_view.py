# from django.views.generic import ListView
# from yumelinkapp.models import User
#
#
# class ProfileView(ListView):
#     model = User
#     template_name = 'yumelink/user_profile.html'
#     context_object_name = 'user_profile'
#
#     def get_queryset(self):
#         return User.objects.all().order_by('name')

# views.py
from django.shortcuts import render
from django.views.generic import ListView
from yumelinkapp.models import User

class ProfileView(ListView):
    model = User
    template_name = 'yumelink/user_profile.html'
    context_object_name = 'user_profile'

    def get_queryset(self):
        # If there's a search query in the GET parameters, filter users
        search_query = self.request.GET.get('search', '')
        if search_query:
            return User.objects.filter(name__icontains=search_query)  # Filter by name
        return User.objects.all().order_by('name')  # Return all users if no search query
