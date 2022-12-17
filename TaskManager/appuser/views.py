from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from TaskManager.appuser.forms import CreateAppUserForm, EditUserForm
from TaskManager.appuser.models import ADMINISTRATOR

USER_PAGINATE = 10
ADMINISTRATOR = ADMINISTRATOR
UserModel = get_user_model()


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


class AppUserView(ListView):
    model = UserModel
    template_name = 'appusers/list-users.html'
    paginate_by = USER_PAGINATE

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionError('Access denied')
        elif request.user.role in (ADMINISTRATOR,):
            dispatch = super().dispatch(request, *args, **kwargs)
            return dispatch
        else:
            raise PermissionError('Access denied')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('username')
        return queryset


class DetailUserView(DetailView):
    model = UserModel
    template_name = 'appusers/details-user.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionError('Access denied')
        elif request.user.role in (ADMINISTRATOR,):
            dispatch = super().dispatch(request, *args, **kwargs)
            return dispatch
        else:
            raise PermissionError('Access denied')


class EditUserView(UpdateView):
    model = UserModel
    form_class = EditUserForm
    template_name = 'appusers/edit-user.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionError('Access denied')
        elif request.user.role in (ADMINISTRATOR,):
            dispatch = super().dispatch(request, *args, **kwargs)
            return dispatch
        else:
            raise PermissionError('Access denied')

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk': self.object.id})
