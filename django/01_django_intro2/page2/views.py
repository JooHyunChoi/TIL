from django.shortcuts import render
import requests
import random
# Create your views here.

def gong(request):
    return render(request , "page2/gong.html")
def index(request):
    return render(request , "page2/index.html")


def throw(request):
    return render(request , "throw.html")
''' 사용자로 부터 정보를 받아서 다시 던져줄 페이지 '''
def catch(request):
    message = request.GET.get('message') 
    ''' GET요청을 통해 들어오면 
    GET 안에 들어옴 딕셔너리 형식으로 들어 옵니다.'''
    context = {
        'message' : message
    }
    return render(request , "page2/catch.html" , context)

def asciiart(request):
    return render(request , "page2/asciiart.html")

def result(request):
# 1. form 태그로 날린 데이터를 받는다. (GET 방식)
    word = request.GET.get('word')
    # 2. ARTII api로 요청을 보내 응답 결과를 text로 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # fonts --> str
    # 3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')
    # 4. fonts(list)안에 들어있는 요소중 하나를 선택해서 font라는 변수에 저장한다.
    font = random.choice(fonts)
    # 5. 위에서 우리가 만든 word와 font를 가지고 다시 요청을 보내 응답 결과를 result에 저장
    result = requests.get(
        f'http://artii.herokuapp.com/make?text={word}&font={font}'
    ).text
    context = {'result': result}
    return render(request, 'page2/result.html', context)


def user_new(request):
    return render(request , 'page2/user_new.html')
''' 실제로는 이렇게 짜지 않는다. 저 세상 코드... '''
def user_create(request):
    user_id = request.POST.get('user_id')
    pwd = request.POST.get('pwd')
    context = {
        'user_id' : user_id,
        'pwd' : pwd
    }
    return render(request , 'page2/user_create.html' , context)


def static_sample(request):
    return render(request , 'page2/static_sample.html')



