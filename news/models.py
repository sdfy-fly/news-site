from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True , verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата')
    slug = models.SlugField(verbose_name='Slug' , unique=True)
    category = models.ForeignKey('Category' , on_delete= models.CASCADE , verbose_name='Категория')
    is_published = models.BooleanField(verbose_name='Опубликовано' , default=False)

    def get_absolute_url(self):
        return reverse('view_news' , kwargs={"slug" : self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            # Newly created object, so set slug
            self.slug = slugify(unidecode(self.title))

        super(News, self).save(*args, **kwargs)
    

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
   