from django.shortcuts import render
import random
import math
from datetime import datetime
#create your views here
# view함수 -> 중간관리자
# 사용자가 접속해서 볼 페이지를 작성한다. 즉, 하나하나의 페이지를 'view'라고 부른다
# view 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다.
# 필수적으로 첫번째 인자는 반드시 request!



# Create your views here.
def index(request): # 첫번쨰 인자 반드시 request
    return render(request , "index.html")

def introduce(request):
    name = "감자"
    ''' render 메소드에 3번째 인자로 변수를 딕셔너리 형태로 넘길 수 있다. '''
    return render(request , "introduce.html" , {'name' : name}) 
def dinner(request):
    menu = ['초밥' , '삼겹살' , '치즈돈까스' ,'순두부찌개']
    pick = random.choice(menu)
    context = {
        'pick' : pick
    }
    return render (request , 'dinner.html' , context)

''' Lorem Picsum 사용해서 랜덤 이미지 보여주는 페이지 만들기 '''
def randomImage(request):
    return render(request , "randomImage.html")

''' 동적 라우팅 '''
def hello(request , name):
    menu = ['초밥' , '삼겹살' , '치즈돈까스' ,'순두부찌개']
    pick = random.choice(menu)
    context = {
        'name' : name,
        'pick' : pick
        }
    return render(request , "hello.html" , context)

''' 실습 1 : 템플릿 변수를 2개 이상 넘겨서 , 이름/나이/취미/특기 등을 여러가지 정보를 표현해 보자'''
def itsme(request,name,age,hobby,specialty):
    context = {
        'name' : name,
        'age' : age,
        'hobby' : hobby,
        'specialty' : specialty
    }
    return render(request , "itsme.html" , context)

''' 실습 2 : 숫자 두개를 동적 라우팅으로 전달 받아서 , 두개의 숫자를 곱해주는 페이지를 만들자'''
def multiple(request , num1 , num2):
    context = {
        'num1' : num1,
        'num2' : num2,
        'num3' : int(num1) * int(num2)
    }
    return render(request , "multiple.html" , context)
''' 실습 3 : 반지름을 인자로 받아서 원의 넓이를 구하는 페이지를 만들자'''
def area(request , num1):
    num = int(num1)
    context = {
        'num' : num,
        'area' : num*num*(math.pi)
    }
    
    return render(request , "area.html" , context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


''' 실습 1 Is it your Birthday ? 
날짜 라이브러리 활용
오늘 날짜와 본인 실제 생일 비교해서 , 맞으면 예! 아니면 아니오!'''
def isitbirthday(request):
    days =datetime.now()
    birthday = False
    if days.month == 7 and days.day == 24:
        birthday = True
    context = {
        'birthday' : birthday
    }
    return render(request, 'isitbirthday.html', context)

''' 실습 2 
회문 판별(팰린드롬 / 문자열 슬라이싱 파트 활용 )
ex) 오디오는 거꾸로 해도 오디오 -> 회문'''
def palindrome(request , text):
    palindrome = False
    if text[:] == text[::-1]:
        palindrome = True
    context = {
        'palindrome' : palindrome
    }
    return render(request , 'palindrome.html' , context)
''' 실습 3
로또 번호 추첨(리스트 + a 활용)
임의로 출력한 로또 번호와 가장 최근에 추첨한 로또 번호 비교해서 당첨여부 확인'''
def lotto(request , nums):
    lottoNums = list(map(int , nums.split(',')))
    winningNums = [18, 34, 39, 43, 44, 45]
    bonusNum = [23]
    count = 0
    for i in lottoNums:
        for j in winningNums:
            if i == j:
                count += 1
    if count == 5:
        for i in lottoNums:
            if i == bonusNum:
                count = 7

    if count == 7:
        rank = '2등'
    elif count == 6:
        rank = '1등'
    elif count >= 3:
        rank = 8-count
    else:
        rank = '꽝'
    context = {
        'num1' : lottoNums[0],
        'num2' : lottoNums[1],
        'num3' : lottoNums[2],
        'num4' : lottoNums[3],
        'num5' : lottoNums[4],
        'num6' : lottoNums[5],
        'rank' : rank
    }
    return render(request , 'lotto.html' , context)
