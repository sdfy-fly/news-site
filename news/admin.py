from django.contrib import admin
from .models import News , Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'category' , 'content' , 'created_at' , 'is_published')
    list_display_links  = ('id' , 'title')
    search_fields = ('title' , 'created_at')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title", )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' )
    list_display_links  = ('id' , 'title' )

admin.site.register(News , NewsAdmin)
admin.site.register(Category , CategoryAdmin)