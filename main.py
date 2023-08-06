# for FastAPI
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def index():
#     return {"Hello": "World"}


# for Flask
from flask import Flask, jsonify

from flask import request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

#Token取得

# YOUR_CHANNEL_ACCESS_TOKEN = "チャネルアクセストークン"
# YOUR_CHANNEL_SECRET = "チャネルシークレット"
# os.getenv()


# 問題なし
# app = Flask(__name__)

# @app.route("/", methods=['GET'])
# def index():
#     return jsonify({"Hello": "World"})

# if __name__ == "__main__":
#     app.run()

app = Flask(__name__)
app.debug = False

line_bot_api = LineBotApi(os.getenv('YOUR_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('YOUR_CHANNEL_SECRET'))
print('その１')
@app.route("/callback", methods=['POST'])
def callback():
    print('その２')
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('その３~4')
    message = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message)
        )


if __name__ == "__main__":
    print('その６')
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)