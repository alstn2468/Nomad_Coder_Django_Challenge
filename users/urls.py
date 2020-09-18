from django.urls import path
from users.views import (
    LoginView,
    LogoutView,
    SignUpView,
    ProfileView,
    PasswordChangeView,
)

app_name = "users"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("change-password", PasswordChangeView.as_view(), name="password"),
]
