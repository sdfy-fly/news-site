from django.urls import path 
from .views import *

urlpatterns = [
    path('', HomeNews.as_view() , name='home') ,
    path('category/<int:category_id>/' , GetCategory.as_view() , name='category'),
    path('news/<slug:slug>' , ViewNews.as_view() , name='view_news'),
    path('add-news' , CreateNews.as_view() , name='add_news'),
]
