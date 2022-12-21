import requests
import string
import os

def item_to_html(item):

    item_string = string.capwords(item['title']) + ' - Size ' + item['size_title'] + ' - £' + item['price']
    item_url = item['url']

    html = f'<a href="{item_url}">{item_string}</a>'

    return html

def send_to_telegram(message, chatID, apiToken):

    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message, 'parse_mode':'html'})
        print(response.text)
    except Exception as e:
        print(e)


