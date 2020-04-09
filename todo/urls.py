from django.urls import path, reverse_lazy
from django.views.generic import CreateView
from todo.models import Todo
from . import views

urlpatterns = [
    path('', views.TodoCreateView.as_view(), name='home')
]
