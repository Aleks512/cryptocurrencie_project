from django.urls import path
from .views import register, profile, delete_account, home

urlpatterns = [
    path('register/', register, name='register'),
    path('delete-account/', delete_account, name='delete-account'),
    path('profile/', profile, name='profile'),
    path('', home, name='home'),
]