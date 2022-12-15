"""TaskManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from TaskManager.exception_handler import handler_error500, handler_error404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('TaskManager.appuser.urls')),
    path('', include('TaskManager.webtask.urls'))
]

handler500 = handler_error500
handler404 = handler_error404
