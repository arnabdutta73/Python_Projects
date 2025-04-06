from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Habit, Task
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'track_it/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'track_it/login.html')

def logout_view(request):
    logout(request)
    return redirect('track_it/login')

def home_view(request):
    return HttpResponse("Welcome to Habit Tracker!")

# Habit Views
class HabitListView(LoginRequiredMixin, ListView):
    model = Habit
    context_object_name = 'habits'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    fields = ['name', 'description', 'tags']
    success_url = reverse_lazy('habit_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    fields = ['name', 'description', 'tags']
    success_url = reverse_lazy('habit_list')

class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    success_url = reverse_lazy('habit_list')

# Task Views
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(habit__user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['habit', 'date', 'completed']
    success_url = reverse_lazy('task_list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['habit', 'date', 'completed']
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')