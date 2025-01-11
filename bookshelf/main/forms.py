from .models import Books
from django.forms import ModelForm, TextInput

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['city', 'nickname', 'title', 'writer', 'description', 'exchange', 'telegram']

        widgets = {
            "city": TextInput(attrs={
                'class': 'input_add',
                'size': '63',
                'maxlength': '63',
            }),
            "nickname": TextInput(attrs={
                'class': 'input_add',
                'size': '63',
                'maxlength': '63',
            }),
            "title": TextInput(attrs={
                'class': 'input_add',
                'size': '63',
                'maxlength': '63',
            }),
            "writer": TextInput(attrs={
                'class': 'input_add',
                'size': '63',
                'maxlength': '50',
            }),
            "description": TextInput(attrs={
                'class': 'input_add',
                'size': '63',
                'maxlength': '250',
            }),
            "exchange": TextInput(attrs={
                'class': 'input_add',
                'size': '63',
                'maxlength': '63',
            }),
            "telegram": TextInput(attrs={
                'class': 'input_add',
                'size': '63',
                'maxlength': '50',
            }),            
        }