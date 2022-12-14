from django.urls import path

from TaskManager.webtask.views import home_page, CreatePersonnelView, CreateMachineView, \
    CreateTaskView, ListPersonnelView, DetailsPersonnelView, ListMachineView, ListTaskView, \
    DetailsTaskView, CreateStepView, DetailsMachineView, EditTaskView, ListStepView, \
    DetailsStepView, EditStepView

urlpatterns = [
    path('', home_page, name='home'),
    path('personnel/', CreatePersonnelView.as_view(), name='create personnel'),
    path('personnel/list/', ListPersonnelView.as_view(), name='list personnel'),
    path('personnel/details/<int:pk>/', DetailsPersonnelView.as_view(), name='detail personnel'),
    path('machine/', CreateMachineView.as_view(), name='create machine'),
    path('machine/list/', ListMachineView.as_view(), name='list machine'),
    path('machine/details/<int:pk>/', DetailsMachineView.as_view(), name='details machine'),
    path('task/', CreateTaskView.as_view(), name='create task'),
    path('task/edit/<int:pk>/', EditTaskView.as_view(), name='edit task'),
    path('task/list/', ListTaskView.as_view(), name='list task'),
    path('task/details/<int:pk>/', DetailsTaskView.as_view(), name='details task'),
    # path('step/', CreateStepView.as_view(), name='create step'),
    path('stepf/<int:pk>/', CreateStepView, name='create step'),
    path('step/list/<int:pk>/', ListStepView.as_view(), name='list step'),
    path('step/details/<int:pk>/', DetailsStepView.as_view(), name='details step'),
    path('step/edit/<int:pk>/', EditStepView.as_view(), name='edit step')
]
