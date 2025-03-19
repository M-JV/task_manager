from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Category
from .forms import Task_Form



# Home Page
def home(request):
    return render(request, 'home.html')

# Listing available tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})

# Displaying task details
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "task_detail.html", {"task": task})

# Creating a new task
def task_creation(request):
    if request.method == "POST":
        form = Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks")
    else:
        form = Task_Form()
    return render(request, "task_create.html", {"form": form})

# Task Completed
def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = "Completed"
    task.save()
    return redirect("tasks")

# Deleting a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    return render(request, "task_confirm_delete.html", {"task": task})

# List of categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {"categories": categories})

# Tasks in a category
def category_tasks(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tasks = Task.objects.filter(category=category)
    return render(request, "category_tasks.html", {"category": category, "tasks": tasks})

# Custom 404 error page
def custom_404(request, exception):
    return render(request, '404.html', status=404)

# Custom 500 error page
def custom_500(request):
    return render(request, '500.html', status=500)

# Custom trigger for 505
def trigger_500(request):
    return 1 / 0
