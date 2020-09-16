from django.urls import path
from users.views import (
    LoginView,
    log_out,
    SignUpView,
)

app_name = "users"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("logout", log_out, name="logout")
]
