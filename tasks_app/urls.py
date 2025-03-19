from django.urls import path
from . import views
from .views import home, task_creation, task_list, task_detail, mark_completed, delete_task, category_list, category_tasks, trigger_500



urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path("tasks/create/", task_creation, name="task_creation"),
    path('tasks/', views.task_list, name='tasks'),
    path("tasks/<int:task_id>/", task_detail, name="task_detail"),
    path("tasks/<int:task_id>/complete/", mark_completed, name="mark_completed"),
    path("tasks/<int:task_id>/delete/", delete_task, name="delete_task"),
    path('categories/', views.category_list, name='categories'),
    path("categories/<int:category_id>/", category_tasks, name="category_tasks"),
    path('trigger-500/', trigger_500, name='trigger_500'),
]
