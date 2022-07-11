from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import ListView , DetailView

from .models import News 
from .forms import NewsForm

class HomeNews(ListView):
    
    """Класс для отображения всех новостей - главная страница"""
    
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self) :
        return News.objects.all()


class GetCategory(ListView):

    """Класс для отображения страницы категорий новостей - страница категории"""

    model = News
    context_object_name = 'news'
    template_name = 'news/category.html'
    paginate_by = 2
    allow_empty = False

    def get_queryset(self) :
        return News.objects.filter(category = self.kwargs['category_id'])


class ViewNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'news/view_news.html'
    paginate_by = 2

# def view_news(request , news_id):

#     context = {
#         # 'news' : News.objects.get(pk=news_id)
#         'news' : get_object_or_404(News , pk=news_id)   
#     }

#     return render(request , 'news/view_news.html' , context)


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

# def index(request):

#     context = {
#         'news' : News.objects.all() 
#     }
#     return render(request , 'news/index.html' , context)

# def get_category(request , category_id) : 
    
#     news = News.objects.filter(category=category_id)

#     context = {
#         'news' : news ,
#     }

#     return render(request , 'news/category.html' , context)


