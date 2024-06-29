from django.forms import ModelForm
from django import forms
from . models import Task

# Forms for the models

#update task
class TaskForm(ModelForm): 
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

#create a task
class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'date_due']
        widgets = {
            'date_due': forms.DateTimeInput(attrs={'type': 'datetime-local', 'color': 'black'})
        }
            
        exclude = ['user']

