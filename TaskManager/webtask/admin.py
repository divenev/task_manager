from django.contrib import admin

from TaskManager.webtask.models import Personnel, Machine, Task, Step


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    pass


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    pass
