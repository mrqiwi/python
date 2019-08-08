#!/usr/bin/python3
# -*- coding: utf-8 -*-

# активация виртуальной среды
# source venv/bin/activate

# установка вебхука
# https://api.telegram.org/bot<token>/setWebhook?url=https://mrqiwi.pythonanywhere.com/

from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
import requests
import json
import re

app = Flask(__name__)
sslify = SSLify(app)

URL = 'https://api.telegram.org/bot<token>/'    

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='bla-bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

def parse_text(text):
   pattern = r'/\w+'
   crypto = re.search(pattern, text).group()
   return crypto 

def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    return price    

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        pattern = r'/\w+'

        if re.search(pattern, message):
            price = get_price(parse_text(message))
            send_message(chat_id, text=price)
        return jsonify(r)
    return '<h1>Welcome!</h1>'    


if __name__ == "__main__":
    app.run()