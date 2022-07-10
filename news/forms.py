from django import forms
from .models import News

import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta: 
        model = News
        fields = ['title' , 'content' , 'category']
        widgets = {
            'title' : forms.TextInput( attrs={
                'placeholder' : 'Введите название'
            }) ,
            'content' : forms.Textarea(attrs={
                'placeholder' : 'Введите содержимое новости' ,
                'rows' : 10, 
                'cols' : 70
            }),
            'category' : forms.Select()
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d' , title) : 
            raise ValidationError('Название не должно начинаться с цифры')
        return title
