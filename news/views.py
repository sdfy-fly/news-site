from django.shortcuts import render
from .models import News , Category


def index(request):

    context = {
        'news' : News.objects.all() 
    }

    return render(request , 'news/index.html' , context)
    

def get_category(request , category_id) : 
    
    news = News.objects.filter(category=category_id)

    context = {
        'news' : news ,
    }

    return render(request , 'news/category.html' , context)


def view_news(request , news_id):

    context = {
        'news' : News.objects.get(pk=news_id)
    }

    return render(request , 'news/view_news.html' , context)
