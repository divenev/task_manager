from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from TaskManager.appuser.forms import CreateAppUserForm, UpdateAppUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(auth_admin.UserAdmin):
    form = UpdateAppUserForm
    add_form = CreateAppUserForm
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    # 'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                    'role'
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)
