from decouple import config
import requests
api_url = 'https://api.telegram.org'
#token = '991657167:AAGUwPA3tdQCar1p9Lql0fX4M5fVMyMyCk8'
token = config('TELEGRAM_BOT')
#chat_id = '936209880'
chat_id = config('CHAT_ID')
text = input('메세지를 입력해주세요 : ')

requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')