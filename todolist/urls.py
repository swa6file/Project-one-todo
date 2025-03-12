"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.template.context_processors import request
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tasks import views
from tasks.views import TaskAPIList, TaskAPIUpdate, TaskAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tasks.urls')),
    path('users/',include('users.urls',namespace='users')),

    #DRF
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #END

    path('support/', include('support.urls'))
]

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Задачи наших пользователей"