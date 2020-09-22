from django.views.generic import FormView, DetailView, RedirectView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from users.forms import LoginForm, SignUpForm, UserChangeForm
from users.models import User


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    pattern_name = "core:home"

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/profile_update.html"
    form_class = UserChangeForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("users:profile", kwargs={"pk": pk})


class PasswordChangeView(BasePasswordChangeView):
    template_name = "users/password_change.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()
        self.request.session.flush()
        logout(self.request)
        return super().form_valid(form)