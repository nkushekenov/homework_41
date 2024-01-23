from email import message_from_bytes
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Task
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'list.html'
    context_object_name = 'tasks'

class CreateTask(SuccessMessageMixin, CreateView):
    model = Task
    fields = '__all__'
    template_name = 'create.html'
    success_url = reverse_lazy('task-list')
    success_message = 'Task added successfully'