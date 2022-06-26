from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название' , widget=forms.TextInput(
        attrs={
            "placeholder" : 'Введите название',
        }
    ))
    content = forms.CharField(label='Содержимое' , widget=forms.Textarea(
        attrs={
            "rows" : 10,
            "cols" : 70,
            "placeholder" : 'Введите содержимое новости'
        }
    ))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all() , 
        label='Категория' ,
        empty_label=None,
    )
    
