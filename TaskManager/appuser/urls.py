from django.urls import path

from TaskManager.appuser.views import LoginUserView, RegisterUserView, LogoutUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='user login'),
    path('register/', RegisterUserView.as_view(), name='user register'),
    path('logouth/', LogoutUserView.as_view(), name='user logout')

]
