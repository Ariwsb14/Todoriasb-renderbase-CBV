from django.shortcuts import render , redirect
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , DeleteView , UpdateView
from django.views.generic import View
# Create your views here.
#task list
class TaskListView(ListView):
    model = Task
    template_name = 'todolist/index.html'
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(user = self.request.user)
        context["tasks"] = tasks
        return context

# creating a task
class TaskCreateView(CreateView):
    model = Task
    template_name = 'todolist/index.html'
    fields = ('title',)
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#delete a task
class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'

#make status of in progress task to comleted status
class TaskCompleteView(UpdateView):
    model = Task
    template_name = 'todolist/index.html'
    fields = ('completed',)
    success_url = '/'
    def form_valid(self, form): 
        form.instance.completed = True
        return super().form_valid(form)

#reset a finished task
class TaskResetView(UpdateView):
    model = Task
    template_name = 'todolist/index.html'
    fields = ('completed',)
    success_url = '/'
    def form_valid(self, form):
        form.instance.completed = False
        return super().form_valid(form)

#edit the title of a task
class TaskEditView(UpdateView):
    model = Task
    template_name = 'todolist/edit.html'
    fields = ('title',)
    success_url = '/'