import json

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('h36DEiW/iRpAgib0ryeNQmVAuKX6eaqEKzCj5QoT/2oXYXnRwFj9hCz0xeAflXyzPsk3lnrjZdsDlYGgXv56B7NMDSDHxgW4/AkLuhl8oNES0ts6/LkRY8EHcHl9YAgLdzn9mm1hw6BfC/psgq7figdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d57f500b5ac8ede281c2b196e1ad547b')

# Rich menu

import requests
import json

headers = {"Authorization":"Bearer 3Ma92PMIfy790Z...","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
          "action": {"type": "message", "text": "up"}
        },
        {
          "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "right"}
        },
        {
          "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
          "action": {"type": "message", "text": "down"}
        },
        {
          "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "left"}
        },
        {
          "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn b"}
        },
        {
          "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn a"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
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

# 預設訊息
@handler.add(FollowEvent)
def handle_follow(event):
    print("in Follow")
    #default = ("可以輸入下列關鍵字，獲得更多資訊喔！\n\n"
    #        "輸入：自我介紹、程式語言、工作經驗、GitHub")
    button_template_message =ButtonsTemplate(
                                    thumbnail_image_url="https://i.imgur.com/eTldj2E.png?1",
                                    title='施柏丞自我介紹Line Rob', 
                                    text='可以透過下列選項了解我喔！',
                                    image_size="cover",
                                    actions=[
                                        MessageTemplateAction(
                                            label='自我介紹', text='自我介紹'   
                                        ),
                                        MessageTemplateAction(
                                            label='程式語言', text='程式語言'
                                        ),
                                        MessageTemplateAction(
                                            label='工作經驗', text='工作經驗'
                                        ),
                                        MessageTemplateAction(
                                            label='Github', text='Github'
                                        ),
                                    ]
                                )
                                
    line_bot_api.reply_message(
        event.reply_token,[
        TextSendMessage(text='您好！我是柏丞，可以透過下列選單了解我更多喔！'), 
        StickerSendMessage(package_id=1, sticker_id=13),
        TemplateSendMessage(alt_text="可以輸入下列關鍵字，獲得更多資訊喔！\n\n輸入：自我介紹、程式語言、工作經驗、GitHub",template=button_template_message)
    ])

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = (event.message.text).lower()

    default = ('您好！我是柏丞 '0x100079'\n\n可以輸入下列關鍵字，獲得更多資訊喔！\n\n輸入：自我介紹、程式語言、工作經驗、GitHub'

    #intro = 

    #language = 

    #experience = 

    #github = ('Line Rob： https://github.com/bocheng47/LINE_bocheng \n ' 
    #        '中央資管系網站(測試中)： https://github.com/bocheng47/ncu_immgt\n '
    #        'Hi-health technology co.： https://github.com/bocheng47/hihealth')

    if 'hello' in msg :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text="哈囉, 祝你有愉快的一天"))

    elif '自我介紹' in msg :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text="哈囉, 我是柏丞"))

    elif '程式語言' in msg :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text="我會的語言有：Python、PHP"))

    elif '工作經驗' in msg :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text="系網站、實習"))

    elif 'github' in msg :
        #uri = "https://github.com/bocheng47/LINE_bocheng" + titleURL['href']
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text=github))
    
    else :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text=default) 
        )
        #line_bot_api.reply_message(event.reply_token,
        #    TextSendMessage(text=event.message.text))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
