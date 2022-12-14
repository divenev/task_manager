from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField, UserCreationForm


UserModel = get_user_model()


class CreateAppUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", )
        field_classes = {"username": UsernameField}
