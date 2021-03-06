from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

# Create your models here.
# django.db의  models에서 상속 받아서 사용한다.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    ''' 원래 대로 라면 새로운 필드를 추가하려고 하면 makemigrations 
        할때 어떤 값을 넣을건지 django가 물어본다.
        기본적으로 blank=False이기 때문이다. 
        blank = True -> 빈 문자열이 들어가도 된다. '''
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
        processors=[Thumbnail(300,420)], # 처리할 작업
        format="JPEG", # 이미지 포멧
        options={'quality' : 90}, # 각종추가 작업
        upload_to = "articles/images", # 저장위치
        # 실제 경로 -> MEDIA/ROOT/articles/images
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] : {self.title} '

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level 에서 MetaData 설정
    class Meta:
        ordering = ['-pk',]

    # 객체 표시 형식 수정
    def __str__(self):
        return self.content