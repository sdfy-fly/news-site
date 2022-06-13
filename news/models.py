from tabnanny import verbose
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True , verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата')
    category = models.ForeignKey('Category' , on_delete= models.CASCADE)

    def __str__(self) : 
        return self.title

    class Meta() :
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория')
    
    def __str__(self) : 
        return self.title
