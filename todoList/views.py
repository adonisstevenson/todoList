from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from .forms import TaskForm, LoginForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .managers import TaskManager
from django.contrib.auth import logout
from django.utils.decorators import method_decorator


class TaskView(TemplateView):

    _manager = TaskManager()

    @method_decorator(login_required, name='dispatch')
    def index(self, request):

        tasks = self._manager.get_tasks(user_id=request.user.id, limit=4)
        template = loader.get_template('index.html')

        return HttpResponse(template.render({'tasks': tasks}, request))


    @method_decorator(login_required, name='dispatch')
    def view_task(self, request, task_id):
        task = self._manager.get_task(request, task_id)
        template = loader.get_template('task.html')

        return HttpResponse(template.render({'task':task}, request))

    @method_decorator(login_required, name='dispatch')
    def new_task(self, request):

        if request.method == "GET":
            form = TaskForm(initial={'task_status': False})

            template = loader.get_template('new_task.html')
            return HttpResponse(template.render({'form': form}, request))

        elif request.method == "POST":

            self._manager.new_task(request)
            response = redirect('/')
            return response

    @method_decorator(login_required, name='dispatch')
    def update_task(self, request, task_id):
        task = self._manager.get_task(request, task_id)

        if request.method == "GET":
            form = TaskForm(instance=task)
            template = loader.get_template('edit_task.html')
            return HttpResponse(template.render({'form': form}, request))

        elif request.method == "POST":

            self._manager.update_task(request, task_id)

            response = redirect(f'/task/{task_id}')
            return response

    @method_decorator(login_required, name='dispatch')
    def delete_task(self, request, task_id):

        self._manager.delete_task(task_id)

        response = redirect('/')
        return response

    @method_decorator(login_required, name='dispatch')
    def task_done(self, request, task_id):
        self._manager.task_done(task_id)

        response = redirect('/')
        return response


class UserView(TemplateView):

    def login(self, request):
        form = LoginForm()

        template = loader.get_template('login.html')
        return HttpResponse(template.render({'form': form}, request))


    def login_validate(self, request):

        form = LoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user is not None:
                auth.login(request, user)
                return redirect('/')

        return HttpResponse('logged in unsuccessfully')

    def logout(self, request):
        logout(request)

        return redirect('/login')
