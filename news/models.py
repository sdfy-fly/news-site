from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True , verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата')
    category = models.ForeignKey('Category' , on_delete= models.CASCADE , verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news' , kwargs={"news_id" : self.pk})

    def __str__(self) : 
        return self.title

    class Meta() :
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория')
    
    def get_absolute_url(self):
        return reverse('category' , kwargs={"category_id" : self.pk})
        
    def __str__(self) : 
        return self.title

    class Meta() :
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
   