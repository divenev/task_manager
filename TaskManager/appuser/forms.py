from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField, UserCreationForm, UserChangeForm
from django import forms

UserModel = get_user_model()


class CreateAppUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username",)
        field_classes = {"username": UsernameField}


class UpdateAppUserForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {"username": UsernameField}


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'role', 'first_name', 'last_name', 'email', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True})
        }

