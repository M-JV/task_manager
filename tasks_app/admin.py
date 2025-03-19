from django.contrib import admin

# Registering my models here.
from .models import Category, Task

# Customizing the admin panel



class Category_Admin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)



class Task_Admin(admin.ModelAdmin):
    list_display = ("title", "status", "priority", "due_date", "category")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description")


admin.site.register(Category)
admin.site.register(Task)
