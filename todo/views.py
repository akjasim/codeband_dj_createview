from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from todo.forms import TodoForm
from todo.models import Todo


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('home')
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['todos'] = Todo.objects.all()
        return context
