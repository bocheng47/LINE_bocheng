import requests

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
    default = """您好！我是柏丞 \U0001F604

可以輸入下列關鍵字，獲得更多資訊喔！

輸入：自我介紹、程式語言、工作經驗、GitHub

或是透過下方選單選取喔～"""
    
    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=True,
        name="Nice richmenu",
        chat_bar_text="Tap here",
        areas=[RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
            action=URIAction(label='Go to line.me', uri='https://line.me'))]
    )
    rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    rich_menu = line_bot_api.get_rich_menu(rich_menu_id)


    button_template_message =ButtonsTemplate(
                                    thumbnail_image_url="https://i.imgur.com/mNnvVVe.jpg",
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
        TextSendMessage(text=default), 
        TemplateSendMessage(alt_text = "電腦板無法顯示選單\U0001F614",template=button_template_message),
        StickerSendMessage(package_id=1, sticker_id=13),
    ])

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = (event.message.text).lower()

    default = """您好！我是柏丞 \U0001F604

可以輸入下列關鍵字，獲得更多資訊喔！

輸入：自我介紹、程式語言、工作經驗、GitHub

或是透過下方選單選取喔～"""

    intro = """我是施柏丞，目前就讀於中央大學資管系

個性外向、熱愛挑戰、充滿好奇心 \U0001F606

平常喜歡看小說、美劇、打排球

也是系學會活動部與資管系排球隊的一員！

很高興認識你！"""

    ability = """我會的程式語言有：Python、PHP、Java、C、SQL、SAS

我會的軟體有：Weka、Xampp、Git、Postman、Anaconda、GitHub Desktop、Sublime

使用過的資料庫有：MySQL

使用過的框架有：Laravel
"""

    experience = """（一）中央資管系網站開發

時間：2019/07-2019/09

職責：負責系網站全端開發與架設、資料上傳、提供網頁架構圖與程式註解。藉此深入學習PHP、MySQL、Laravel、Git共同開發、MVC架構；在這5人團隊中，我負責團隊的組織，以及與系辦接洽的工作。並從中學習團隊間的互相合作，以及一起討論UI/UX設計，取得共識，並互相指導，提升技術能力。


(二) 您好健康有限公司(程式設計實習生)

時間：2018/08-2019/02

職責：負責網頁前端與後端設計、管理與開發後台、產品測試、UI設計；在團隊中，我常常負責支援公司的工程師，以及對產品提出具體性的建議，也因為我的實質建議，在產品及Code設計也獲得改善，在大多時候需要獨自思考並解決問題，以及如何跳脫框架思考。在過程中建立工作上的自主性、創意和成長經驗。
"""

    github = """Line Rob： https://github.com/bocheng47/LINE_bocheng

fifa19資料分析: https://github.com/bocheng47/fifa19_data_analysis

演算法視覺化 Sort_Visualization： https://github.com/bocheng47/Sort_Visualization

Knight Tour List Comprehension： https://github.com/bocheng47/Knight_tour_List_Comprehension"""

    button_template_message =ButtonsTemplate(
        thumbnail_image_url="https://i.imgur.com/mNnvVVe.jpg",
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

    if ('hello' in msg) or ('早安' in msg) or ('你好' in msg):
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text="哈囉, 祝你有愉快的一天"))

    elif '自我介紹' in msg :
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=intro),
            StickerSendMessage(package_id=1, sticker_id=114),])

    elif '程式語言' in msg :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text=ability))

    elif '工作經驗' in msg :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text=experience))

    elif 'github' in msg :
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text=github))
    
    else :
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=default),
            TemplateSendMessage(alt_text=default,template=button_template_message) 
        ])

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
