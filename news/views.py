from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView , CreateView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib import messages


from .models import News 
from .forms import NewsForm

class HomeNews(ListView):
    
    """Класс для отображения всех новостей - главная страница"""
    
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self) :
        return News.objects.filter(is_published = True)


class GetCategory(ListView):

    """Класс для отображения страницы категорий новостей - страница категории"""

    model = News
    context_object_name = 'news'
    template_name = 'news/category.html'
    paginate_by = 3
    allow_empty = False

    def get_queryset(self) :
        return News.objects.filter(is_published = True ,
                category = self.kwargs['category_id'])


class ViewNews(DetailView):

    """Класс для отображения страницы отдельной новости - страница новости"""

    model = News
    context_object_name = 'news'
    template_name = 'news/view_news.html'


class CreateNews(CreateView):

    """Класс для добавления новости на сайт - страница с формой добавления новости"""

    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')


def register(request):
    
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username = username).exists() :
            messages.info(request, 'Username already used.')
            return redirect('register')
        else : 
            user = User.objects.create_user(username=username,password=password)
            user.save()
            messages.success(request, 'Register was successfully.')
            return redirect('login')


    return render(request , 'news/register.html')

def login(request):
    return render(request , 'news/login.html')