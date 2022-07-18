from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta: 
        model = News
        fields = ['title' , 'content' , 'category']
        widgets = {
            'title' : forms.TextInput( attrs={
                'placeholder' : 'Введите название',
                'class' : 'input__form',
            }) ,
            'content' : forms.Textarea(attrs={
                'placeholder' : 'Введите содержимое новости' ,
                'rows' : 10, 
                'cols' : 70,
                'class' : 'input__form',
            }),
            'category' : forms.Select( attrs={
                'class' : 'input__form',
            })
        }
