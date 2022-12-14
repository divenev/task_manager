from django import forms

from TaskManager.webtask.models import Task, Step, Personnel


class EditPersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'


class DelPersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (['name', 'start_date', 'status', 'requirement', 'description', 'personnel_id', 'profile_id'])
        widgets = {
            'profile_id': forms.HiddenInput(),
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (['name', 'start_date', 'status', 'requirement', 'description', 'personnel_id', 'profile_id'])
        widgets = {
            'profile_id': forms.HiddenInput(),
        }


class CreateStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = '__all__'
        widgets = {
            'task_id': forms.HiddenInput(),
        }


class UpdateStepForm(CreateStepForm):
    pass
