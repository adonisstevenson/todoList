import django.forms
from django.forms import *
from .models import Task, models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class TaskForm(ModelForm):

    task_title = django.forms.CharField(max_length=100,
                                        widget=django.forms.TextInput(attrs={'class': 'form-control'}))

    task_text = django.forms.CharField(max_length=1000,
                                       widget=django.forms.Textarea(attrs={'class': 'form-control'}))


    class Meta:
        model = Task

        labels = {
            'task_status': _('Task done?')
        }

        fields = ['task_title', 'task_text', 'task_date', 'task_status']


class LoginForm(forms.Form):

    username = django.forms.CharField(max_length=50,
                                      widget=django.forms.TextInput(attrs={'class': 'form-control'}))
    password = django.forms.CharField(max_length=50,
                                      widget=django.forms.PasswordInput(attrs={'class': 'form-control'}))

