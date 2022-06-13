from django.shortcuts import render
from .models import News
# Create your views here.

def index(request):

    context = News.objects.all()


    return render(request , 'news/index.html' , context={'news' : context})
    