import requests
import json
from flask import Flask
from flask import request
from flask import Response
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

token = 'TELEGRAM_API_KEY_HERE'

app = Flask(__name__)

interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')

agent = Agent.load('./models/dialogue', interpreter = interpreter, action_endpoint ='http://localhost:5055/webhook')
def applyAi(message):
    responses = agent.handle_message(message)
    text = []
    if responses:
        for response in responses:
            text.append(response["text"])
    return text


def parse_msg(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    return chat_id,txt

def send_message(chat_id,messages=[]):
    url = 'https://api.telegram.org/bot'+token+'/sendMessage'
    if messages:
        for message in messages:
            payload = {'chat_id' : chat_id,'text' : message}
            requests.post(url,json=payload)
    return True


@app.route('/',methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        msg = request.get_json()
        chat_id , message = parse_msg(msg)
        response_messages = applyAi(message)
        send_message(chat_id,response_messages)
        return Response('ok',status=200)
    else:
        return '<h1>HELLO</h1>'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
