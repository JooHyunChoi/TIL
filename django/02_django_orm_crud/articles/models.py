from django.db import models

# Create your models here.
'''django.db.model.Model  클래스를 상속 받아서 모델을 정의 함! '''
class Article(models.Model):
    ''' id(PK)는 인스턴스 생성과 함께 자동으로 부여된다. 
    CharField에서 max_length는 필수 인자
    장고 내부에서 데이터 유효성 검증을 할때 사용'''
    title = models.CharField(max_length=30)
    '''긴 문자열은 TextField 사용'''
    content = models.TextField()

    '''auto_now_add = True  -> 인스턴스 최소 생성 시각'''
    create_at = models.DateTimeField(auto_now_add=True)
    '''auto_now = True  -> 인스턴스 최종 수정 시각(업데이트 됬음)'''
    #updated_at = models.DateTimeField(auto_now=True)
    
    '''객체를 표시하는 형식 커스터 마이징 '''
    def __str__(self):
        return f'[{self.pk}] : {self.title}'
    