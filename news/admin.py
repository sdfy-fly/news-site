from django.contrib import admin
from .models import News , Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'content' , 'created_at')
    list_display_link = ('id' , 'title' )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' )
    list_display_link = ('id' , 'title' )

admin.site.register(News , NewsAdmin)
admin.site.register(Category , CategoryAdmin)