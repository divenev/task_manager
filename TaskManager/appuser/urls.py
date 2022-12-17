from django.urls import path

from TaskManager.appuser.views import LoginUserView, RegisterUserView, LogoutUserView, \
    AppUserView, DetailUserView, EditUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='user login'),
    path('register/', RegisterUserView.as_view(), name='user register'),
    path('logouth/', LogoutUserView.as_view(), name='user logout'),
    path('list/', AppUserView.as_view(), name='user list'),
    path('details/<int:pk>/', DetailUserView.as_view(), name='user details'),
    path('edit/<int:pk>/', EditUserView.as_view(), name='user edit'),
]
