from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Adicionar nova tarefa....'}))

    class Meta:
        model = Task
        fields = '__all__'

