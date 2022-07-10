from django.shortcuts import render , get_object_or_404 , redirect
from .models import News , Category
from .forms import NewsForm

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
        # 'news' : News.objects.get(pk=news_id)
        'news' : get_object_or_404(News , pk=news_id)   
    }

    return render(request , 'news/view_news.html' , context)


def add_news(request):
    
    if request.method == 'POST' :
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)      
    else : 
        form = NewsForm()
    
    context = {
        'form' : form
    }

    return render(request , 'news/add_news.html' , context)