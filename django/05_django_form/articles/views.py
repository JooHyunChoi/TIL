from django.shortcuts import render, redirect, get_object_or_404
from .models import Article , Comment
from .forms import ArticleForm,CommentForm
from IPython import embed
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import hashlib


# Create your views here.

def index(request):
    #embed()
    # if request.user.is_authenticated:
    #     gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
    # else:
    #     gravatar_url = None

    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method=="POST":
        # Binding  과정
        # Form 인스턴스를 생성하고, 전달받은 데이터를 채운다.
        # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.
        form = ArticleForm(request.POST)
        
        # embed()
        # 유효성 검증
        if form.is_valid():
            article = form.save()
            # 유효성 검증이 끝난 form은 dict 형태로 뽑혀 나온다.
            # cleaned_data 를 통해 dict 안의 데이터를 검증한다.
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)

            return redirect('articles:detail', article.pk)
    
    else :
        form = ArticleForm()
    # Form으로 전달 받는 형태가 2가지
    # 1. GET 요청 -> 비어있는 Form 전달
    # 2. 유효성 검증 실패 -> 에러 메시지도 담겨서 Form 전달        
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
                                # Class    / PK 값
    article = get_object_or_404(Article, pk=article_pk)
    #comments = article.comment_set.all()
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'comment_form' : comment_form,
        'comments' : comments,
        'article' : article,
        #'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article_pk)

    else :
        # 빈 값이 아닌 Form의 데이터를 넣어 주는 부분
        form = ArticleForm(instance=article)

    # 2가지 Form 형식
    # 1. GET 요청 -> 초기값을 Form에 넣어서 사용자에게 던져줌
    # 2. POST -> is_valid가 False 가 리턴되었을때, 
    #            오류 메시지를 포함해서 사용자에게 던져줌
    context = {
        'form' : form,
    }
    # update와 create 로직에서 동일한 form을 던져주기 때문에 create.html을 랜더링한다.
    return render(request, 'articles/form.html', context)


    # 댓글 생성 뷰 함수
@login_required
#@require_POST
def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # Post로 받은 경우 
    if request.method == 'POST':
        #comment = Comment()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #save method에 선택인자가 있습니다. 기본값 commit = true
            # 디비에 바로 저장되는것을 막아준다.
            comment = comment_form.save(commit = False)
            comment.article = article
            comment.save()
    # 로그인 안했을 경우

    return redirect('articles:detail', article.pk)

# 댓글 삭제 뷰 함수
#@login_required
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article.pk)