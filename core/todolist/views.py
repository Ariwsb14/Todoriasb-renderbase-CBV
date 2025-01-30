from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'todolist/index.html'
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all(user = self.request.user)
        return context



