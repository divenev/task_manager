from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum


class ChoicesEnum(Enum):

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


MAX_LENGTH_USER = 25
MIN_LENGTH_USER = 3
MAX_LENGTH_STATUS = 25
ADMINISTRATOR = 'administrator'
MANAGER = 'manager'
STAFF = 'staff'
READ_ONLY = 'read_only'
WITHOUT_DELETE = 'without_delete'


class GroupChoices(ChoicesEnum, Enum):
    administrator = ADMINISTRATOR
    manager = MANAGER
    without_delete = WITHOUT_DELETE
    staff = STAFF
    read_only = READ_ONLY


class AppUser(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=MAX_LENGTH_USER
    )

    role = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        default=STAFF,
        choices=GroupChoices.choices()
    )

    USERNAME_FIELD = 'username'
