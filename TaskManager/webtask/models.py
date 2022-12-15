from enum import Enum

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from TaskManager.appuser.models import AppUser, ChoicesEnum

INTERNAL_ID = 10
MAX_LENGTH_NAMES = 30
MAX_LENGTH_LOCATION = 150
MIN_REQUIREMENT_CHARS = 10
MAX_LENGTH_STATUS = 25
PRICE_FOR_DAY = 1
MIN_LEAD_TIME_IN_DAYS = 1
MIN_STEP_PRIORITY = 1
CREATED = 'created'
IN_PROGRESS = 'in_progress'
FROZEN = 'frozen'
CLOSED = 'closed'
RETURNED = 'returned'


def min_requirement_chars(value):
    if len(value) < MIN_REQUIREMENT_CHARS:
        raise ValidationError('You must describe the requirement (min 10 characters)')


class TaskStatusChoices(ChoicesEnum, Enum):
    created = CREATED
    in_progress = IN_PROGRESS
    frozen = FROZEN
    closed = CLOSED


class StepStatusChoices(ChoicesEnum, Enum):
    created = CREATED
    in_progress = IN_PROGRESS
    returned = RETURNED
    frozen = FROZEN
    closed = CLOSED


class Personnel(models.Model):
    internal_id = models.IntegerField(
        unique=True,
        null=False,
        blank=False
    )

    name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False
    )

    family = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False
    )

    position = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False
    )

    price_for_day = models.FloatField(
        validators=(
            MinValueValidator(PRICE_FOR_DAY),
        ),
        null=False,
        blank=False
    )

    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True
    )

    profile_id = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='registered user'
    )

    def __str__(self):
        return f'№{self.internal_id} - {self.name} {self.family}'


class Machine(models.Model):
    internal_id = models.IntegerField(
        unique=True,
        null=False,
        blank=False
    )

    brand = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False
    )

    model = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False
    )

    license = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False
    )

    price_for_day = models.FloatField(
        validators=(
            MinValueValidator(PRICE_FOR_DAY),
        ),
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'№{self.internal_id} - {self.brand} {self.model} '


class Task(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        unique=True,
        null=False,
        blank=False,
        verbose_name='name'
    )

    start_date = models.DateField(
        null=False,
        blank=False,
    )

    status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        default=CREATED,
        choices=TaskStatusChoices.choices()
    )

    requirement = models.TextField(
        validators=(
            min_requirement_chars,
        ),
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    personnel_id = models.ForeignKey(
        Personnel,
        on_delete=models.RESTRICT,
        verbose_name='Manager'
    )

    profile_id = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
        verbose_name='created by'
    )

    def __str__(self):
        return f'{self.name} - {self.start_date} - {self.status}'


class Step(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False
    )

    requirement = models.TextField(
        validators=(
            min_requirement_chars,
        ),
        null=False,
        blank=False
    )

    implementation = models.TextField(
        null=True,
        blank=True
    )

    lead_time_in_days = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    status = models.CharField(
        max_length=MAX_LENGTH_STATUS,
        default=CREATED,
        choices=StepStatusChoices.choices()
    )

    step_priority = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    comment = models.TextField(
        null=True,
        blank=True
    )

    personnel_id = models.ForeignKey(
        Personnel,
        on_delete=models.RESTRICT,
        verbose_name='Executor'
    )

    machine_id = models.ForeignKey(
        Machine,
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )

    task_id = models.ForeignKey(
        Task,
        on_delete=models.RESTRICT,
        null=False,
        blank=False
    )

    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name} - {self.status}'
