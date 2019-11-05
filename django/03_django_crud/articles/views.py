from django.shortcuts import render , redirect
from .models import Article

# Create your views here.
def index(request):
    # return(request, 'articles/index.html')
    article = Article.objects.all()[::-1]
    context = {'articles' : article}
    return render(request, 'articles/index.html' , context)
''' 사용자에게 게시글 작성 폼을 보야주는 함수'''
def new(request):
    return render(request, 'articles/new.html')
''' 사용자로부터 데이터를 받아서 db에 저장하는 함수 '''
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title = title , content = content)
    article.save()

    return redirect('/articles/')

''' 게시글 상세 정보를 가져오는 함수 '''
def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request , 'articles/detail.html' , context)

