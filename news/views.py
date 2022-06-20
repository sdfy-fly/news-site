from django.shortcuts import render
from .models import News , Category


def index(request):

    context = {
        'news' : News.objects.all() ,
        'categories' : Category.objects.all() 
    }

    return render(request , 'news/index.html' , context)
    

def get_carygory(request , category_id) : 
    
    news = News.objects.filter(category=category_id)
    categories = Category.objects.all()
    
    context = {
        'news' : news ,
        'categories' : categories ,
    }

    return render(request , 'news/category.html' , context)