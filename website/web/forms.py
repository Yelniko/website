from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'input', 'output', 'complexity']
        widgets = {
            'name': TextInput(attrs={
                'class': 'input l',
                'placeholder': ' Enter name task',
            }),
            'description': Textarea(attrs={
                'class': 'input input1',
                'placeholder': 'Enter description',
            }),
            'input': Textarea(attrs={
                'class': 'input input1',
                'placeholder': 'Enter input',
            }),
            'output': Textarea(attrs={
                'class': 'input input1',
                'placeholder': 'Enter output',
            }),
            'complexity': Select(),
        }


class ForumForm(ModelForm):
    class Meta:
        model = SubjectForum
        fields = ['subject']
        widgets = {
            'subject': TextInput(attrs={
                'class': 'input l',
                'placeholder': 'Enter subject'
            })
        }


class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ['name', 'text']
        widgets = {
            'name': TextInput(attrs={
                'class': 'input l',
                'placeholder': 'Enter name news'
            }),
            'text': Textarea(attrs={
                'class': 'input input1',
                'placeholder': 'Enter text',
            }),
        }
