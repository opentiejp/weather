import os

import requests
from dotenv import load_dotenv


def line_notify(message):
    """LINE Notify APIを使用してメッセージを送信"""

    load_dotenv()
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {os.getenv("LINE_TOKEN")}'}
    payload = {'message': message}
    requests.post(line_notify_api, headers=headers, data=payload)
