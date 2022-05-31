from .models import Task
from django.forms import ModelForm, TextInput, DateTimeInput,Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['titl', 'gam', 'numbers', 'adres', 'time', 'wont']
        widgets = {
            "titl": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Консоль'
            }),
            "gam": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Игры'
            }),
            "numbers": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'
            }),
            "adres": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            "time": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата '
            }),
            "wont": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время'
            })
        }
