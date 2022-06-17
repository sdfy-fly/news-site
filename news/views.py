from django.shortcuts import render
from .models import News , Category


def index(request):

    context = {
        'news' : News.objects.all() ,
        'categories' : Category.objects.all() 
    }


    return render(request , 'news/index.html' , context)
    