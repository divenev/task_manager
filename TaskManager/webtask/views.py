from builtins import super

from django.contrib.auth import get_user_model
from django.db.models import RestrictedError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from TaskManager.webtask.forms import CreateTaskForm, CreateStepForm, UpdateTaskForm, UpdateStepForm, \
    EditPersonnelForm, DelPersonnelForm
from TaskManager.webtask.models import Personnel, Machine, Task, Step, CREATED, \
    IN_PROGRESS, FROZEN

UserModel = get_user_model()
PAGINATE_BY = 8


def home_page(request):
    context = {
        'user': request.user
    }
    return render(request, 'webtask/home-page.html', context)


def filter_personnel_id(user_id):
    try:
        result = Personnel.objects.get(profile_id=user_id).pk
    except:
        result = None
    return result


class CreatePersonnelView(CreateView):
    model = Personnel
    fields = ['internal_id', 'name', 'family', 'position', 'price_for_day', 'location', 'profile_id']
    template_name = 'webtask/create-personnel.html'
    success_url = reverse_lazy('home')


class ListPersonnelView(ListView):
    model = Personnel
    template_name = 'webtask/list-personnel.html'
    paginate_by = PAGINATE_BY


class DetailsPersonnelView(DetailView):
    model = Personnel
    template_name = 'webtask/details-personnel.html'


class EditPersonnelView(UpdateView):
    model = Personnel
    form_class = EditPersonnelForm
    template_name = 'webtask/edit-personnel.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('details personnel', kwargs={'pk': self.object.id})


# class DelPersonnelView(DeleteView):
#     model = Personnel
#     template_name = 'webtask/del-personnel.html'
#     success_url = reverse_lazy('list personnel')
#     # TODO on failed deletion it shows the error


def DeletePersonnelView(request, pk):
    personnel = Personnel.objects.get(pk=pk)

    if request.method == 'GET':
        form = DelPersonnelForm(instance=personnel)
    else:
        form = DelPersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            try:
                form.save()
            except RestrictedError:
                context = {
                    'message': f'The employee can\'t be deleted.'
                }
                return render(request, 'webtask/error_template.html', context)
            return redirect('list personnel')

    context = {
        'form': form,
        'object': personnel
    }
    return render(request, 'webtask/del-personnel.html', context)


class CreateMachineView(CreateView):
    model = Machine
    fields = '__all__'
    template_name = 'webtask/create-machine.html'
    success_url = reverse_lazy('home')


class DetailsMachineView(DetailView):
    model = Machine
    template_name = 'webtask/details-machine.html'


class ListMachineView(ListView):
    model = Machine
    template_name = 'webtask/list-machine.html'
    paginate_by = PAGINATE_BY


class CreateTaskView(CreateView):
    form_class = CreateTaskForm
    template_name = 'webtask/create-task.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        if form.fields['profile_id']:
            form.fields['profile_id'].initial = self.request.user.pk
        return form

    def get_success_url(self):
        return reverse_lazy('details task', kwargs={'pk': self.object.id})


class EditTaskView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'webtask/edit-task.html'

    def get_success_url(self):
        return reverse_lazy('details task', kwargs={'pk': self.object.id})


class ListTaskView(ListView):
    model = Task
    template_name = 'webtask/list-task.html'
    paginate_by = PAGINATE_BY

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('start_date')
        queryset = queryset.filter(profile_id=self.request.user.pk)
        queryset = queryset.filter(status__in=[CREATED, IN_PROGRESS, FROZEN])

        if self.__get_search():
            queryset = queryset.filter(name__icontains=self.__get_search())

        return queryset

    def __get_search(self):
        search = self.request.GET.get('search', None)
        return search


class DetailsTaskView(DetailView):
    model = Task
    template_name = 'webtask/details-task.html'


def CreateStepView(request, **kwargs):
    if 'pk' in kwargs:
        task_id = kwargs['pk']
    else:
        return redirect('list task')
    if request.method == 'GET':
        form = CreateStepForm()
        if form.fields['task_id']:
            form.fields['task_id'].initial = task_id

    else:
        form = CreateStepForm(request.POST)
        a = request.POST
        if form.is_valid():
            form.save()
            return redirect('details task', task_id)

    context = {
        'form': form,
        'task_id': task_id,
    }
    return render(request, 'webtask/create-step.html', context)


class ListStepView(ListView):
    model = Step
    template_name = 'webtask/list-step.html'
    paginate_by = PAGINATE_BY

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('step_priority')
        if 'pk' in self.kwargs:
            task_id = self.kwargs['pk']
        else:
            task_id = None

        queryset = queryset.filter(task_id=task_id)

        if self.__get_search():
            queryset = queryset.filter(name__icontains=self.__get_search())

        return queryset

    def __get_search(self):
        search = self.request.GET.get('search', None)
        return search


class ListStepForEmplView(ListView):
    model = Step
    template_name = 'webtask/list-step.html'
    paginate_by = PAGINATE_BY

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('step_priority')
        personnel_id = filter_personnel_id(self.request.user.pk)
        queryset = queryset.filter(personnel_id=personnel_id)

        if self.__get_search():
            queryset = queryset.filter(name__icontains=self.__get_search())

        return queryset

    def __get_search(self):
        search = self.request.GET.get('search', None)
        return search


class DetailsStepView(DetailView):
    model = Step
    template_name = 'webtask/details-step.html'


class EditStepView(UpdateView):
    model = Step
    form_class = UpdateStepForm
    template_name = 'webtask/edit-step.html'

    def get_success_url(self):
        return reverse_lazy('details step', kwargs={'pk': self.object.id})
