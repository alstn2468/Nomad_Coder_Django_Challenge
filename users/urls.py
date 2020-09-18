from django.urls import path
from users.views import (
    LoginView,
    LogoutView,
    SignUpView,
    ProfileDetailView,
    ProfileUpdateView,
    PasswordChangeView,
)

app_name = "users"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("profile/<int:pk>", ProfileDetailView.as_view(), name="profile"),
    path("update/<int:pk>", ProfileUpdateView.as_view(), name="update"),
    path("change-password", PasswordChangeView.as_view(), name="password"),
]
