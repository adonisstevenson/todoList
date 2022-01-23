from django.urls import path
from .models import Task

from . import views

urlpatterns = [
    path('login', views.UserView().login, name='login'),
    path('login/validate', views.UserView().login_validate, name='login_validate'),
    path('logout', views.UserView().logout, name='logout'),

    path('', views.TaskView().index, name='index'),
    path('task/<int:task_id>', views.TaskView().view_task, name='task'),
    path('task/<int:task_id>/delete', views.TaskView().delete_task, name='delete_task'),
    path('task/<int:task_id>/update', views.TaskView().update_task, name='update_task'),
    path('task/<int:task_id>/done', views.TaskView().task_done, name='task_done'),
    path('task/new', views.TaskView().new_task, name='task_new'),

]
