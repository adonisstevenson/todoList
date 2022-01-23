from .models import Task
from .forms import TaskForm

class TaskManager(Task):

    __task = Task

    def get_task(self, request, task_id):

        task = self.__task.objects.get(id=task_id, user_id=request.user.id)

        return task

    def get_tasks(self, user_id, limit=False):

        if limit is not False:
            tasks = self.__task.objects.filter(user_id=user_id).order_by('-id')
        else:
            tasks = self.__task.objects.filter(user_id=user_id).order_by('-id')[:5]

        return tasks

    def delete_task(self, task_id):
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute(f'DELETE FROM "todoList_task" WHERE id={task_id}')


        # self.__task.objects.filter(pk=task_id).delete()

    def new_task(self, request):
        form = TaskForm(request.POST, request.FILES, initial={'user_id': request.user.id})

        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user_id = request.user.id
            new_task.save()

    def update_task(self, request, task_id):

        task = self.__task.objects.get(id=task_id)
        form = TaskForm(request.POST, request.FILES, instance=task)

        if form.is_valid():
            edited_task = form.save(commit=False)
            edited_task.user_id = request.user.id
            edited_task.save()


    def task_done(self, task_id):
        task = self.__task.objects.get(id=task_id)
        task.task_status = True
        task.save()

