from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class Hashtag(models.Model):
    content = models.TextField(unique=True)

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles',
    blank=True)
    hashtags = models.ManyToManyField(Hashtag,blank=True)
    
    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.title}] {self.content}'
    class Meta:
        ordering = ['-pk',]

class Comment(models.Model):
    #Model level에서 메타데이터 옵션 설정-> 정렬 기능 사용 
    class Meta:
        ordering = ['-pk',]
    #객체 표현 방식 
    def __str__(self):
        return self.content
        
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
