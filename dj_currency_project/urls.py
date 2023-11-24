from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from users.views import WebAppLoginView
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("crypto.urls")),
    path("", include("users.urls")),
    path('login/', WebAppLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

