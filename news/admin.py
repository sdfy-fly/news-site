from django.contrib import admin
from .models import News , Category

# Register your models here.
@admin.register(News)
class NewsAdmin():
    list_display = ('id' , 'title' , 'content' , 'created_at')
    list_display_link = ('id' , 'title' )


@admin.register(Category)
class CategoryAdmin():
    list_display = ('id' , 'title' )
    list_display_link = ('id' , 'title' )