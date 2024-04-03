from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'test', 'complexity']
        widgets = {
            'name': TextInput(attrs={
                'class': 'input l',
                'placeholder': ' Enter name task',
            }),
            'description': Textarea(attrs={
                'class': 'input input1',
                'placeholder': 'Enter description',
            }),
            'test': Textarea(attrs={
                'class': 'input input1',
                'placeholder': 'Enter test',
            }),
            'complexity': Select(),
        }
