from .models import  Kommet
from .models import Rent
from  .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class KommetForms(ModelForm):
    class Meta:
        model = Kommet
        fields = ['plus', 'minus', 'full_text', 'date']

        widgets = {
            "plus": TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Приемущества'
            }),
            "minus": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Недостатки'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            })
        }

class RentForms(ModelForm):
    class Meta:
        model = Rent
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Недостатки'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            })
        }

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['consol', 'about_game', 'set_game']
