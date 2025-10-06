from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
     # Habits
    path('habits/', views.HabitListView.as_view(), name='habit_list'),
    path('habits/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habits/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit_delete'),

    # Tasks
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
