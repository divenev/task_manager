from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField, UserCreationForm
from django import forms
from django.urls import reverse_lazy

UserModel = get_user_model()


class CreateAppUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username",)
        field_classes = {"username": UsernameField}


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'role', 'first_name', 'last_name', 'email', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True})
        }

