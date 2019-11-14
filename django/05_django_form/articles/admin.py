from django.contrib import admin
from .models import Article
from .models import Comment
from .models import Hashtag
# Register your models here.
# class ArticleAdmin():


# admin.site.register()

class HashtagAdmin(admin.ModelAdmin):
    list_display=('content',)



admin.site.register(Hashtag, HashtagAdmin)
