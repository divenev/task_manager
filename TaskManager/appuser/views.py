from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView


from django.urls import reverse_lazy
from django.views.generic import CreateView

from TaskManager.appuser.forms import CreateAppUserForm


class LoginUserView(LoginView):
    template_name = 'appusers/user-login.html'


class RegisterUserView(CreateView):
    template_name = 'appusers/user-register.html'
    form_class = CreateAppUserForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')
