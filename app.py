from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
# LINE BOT info
line_bot_api = LineBotApi(
    "EHYRboTyDKqEPZrKGw5gxh2UcxyeS4U2UDRDfYNWjggXcMwZsyakEWZHm+uZFyR9TCo5VxDeQ2zKq/CKa2tSlKTXx8haFo4jOzoSJL4SFoBMuOU2RA35Rv+Y+0IawtPsgdFPf4LW2OI0YlLIIJpvlQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("836a2b5b4cb5cc27d0d882247551867c")


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
