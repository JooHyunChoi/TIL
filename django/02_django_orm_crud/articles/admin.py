from django.contrib import admin
from .models import Article

# Register your models here.


'''Register your models here'''
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk' , 'title' , 'content' , 'create_at',)
    list_display_links = ('title',)
    list_filter = ('create_at',)
    list_editable = ('content',)
    list_per_page = 2

admin.site.register(Article,ArticleAdmin)
