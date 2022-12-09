from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import os
app = Flask(__name__)
# LINE BOT info
line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACESS_TOKEN'))
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent)
def handle_message(event):
    message_type = event.message.type
    user_id = event.source.user_id
    reply_token = event.reply_token
    message = "CC" + event.message.text
    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
