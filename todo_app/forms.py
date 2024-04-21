# forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_title', 'entry']
        labels = {
            'task_title': 'Task Title',
            'entry': 'Task Description',
        }
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Task Title'}),
            'entry': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Task Description', 'rows': 3}),
        }
