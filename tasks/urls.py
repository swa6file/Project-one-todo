from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/',views.tasks,name='taski'),
    path('delete-task/<str:name>/',views.delete_task,name='delete'),
    path('update-task/<str:name>/',views.update,name='update'),
    path('cancel-update/<str:name>/',views.cancel_update,name='cancel-update')
]