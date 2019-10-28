from flask import Flask, render_template,request
from decouple import config
import requests
import random

app = Flask(__name__)
api_url = 'https://api.telegram.org'
#token = '991657167:AAGUwPA3tdQCar1p9Lql0fX4M5fVMyMyCk8'
token = config('TELEGRAM_BOT')
#chat_id = '936209880'
chat_id = config('CHAT_ID')

@app.route('/')
def hello():
    return "hello Joo"


@app.route('/write')
def write():
    return render_template("write.html")

@app.route("/send")
def send():
    text = request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '<h2>메제지 전송 완료<h2>'


# 텔레그램 서버가 우리 서버에게 HTTP POST여청을 통해
# 사용자 메시지 정보를 받으라고 전달해 주는것
# 우리가 status 200을 리턴을 해줘야 텔레그램이 죽어 더이상 전송을 하지 않는자.
# 200 을 안알려주면 계속 post요청을 여러번 보낸다.

def lotto():
    lottoNum = [aa for aa in range(1,47)]
    lotto = random.sample(lottoNum,6)
    # sortedLotto = sorted(lotto)
    lotto.sort()
    lotto = list(map(str , lotto))
    txtlotto = ' , '.join(lotto)
    print(txtlotto)
    return txtlotto


@app.route(f'/{token}' , methods=['POST'])
# 이거는 텔레그램이 Post만 되게끔 만들어져 있음 
def telegram():
    #1. 메아리 기능 
    #1.1 request.get_json() 구조 확인하기
    print(request.get_json())
    # 1.2 사용자 아이디 , 텍스트 가지고 오기
    chat_id = request.get_json().get('message').get('from').get('id')
    text = request.get_json().get('message').get('text')
    if text == '/로또':
        #lotto = "1,2,3,4,5,6"
        #lotto = lotto()
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={lotto()}')

    #1.3 텔레그햄 API 에게 요청을 보내서 답변해주기
    echo = str(chat_id) + "님의 에코입니다. : " + text
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={echo}')

    # 로또 기능
    # 사용자가 '/로또' 라고 말하면 랜덤으로 번호 6개 뽑아서 돌려주기
    # 나머지 경우에는 메아리 ~
    





    return '',200 ##200상태 코드는  정상적으로 받았다 라는 뜻





if __name__ == "__main__":
    app.run(debug = True)