#  for simplifying creation, validation, and rendering forms for my models

from django import forms
from .models import Task

class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority', 'category']
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(choices=Task.STATUS_CHOICE),
            "priority": forms.Select(choices=Task.PRIORITY_CHOICE),
    }

