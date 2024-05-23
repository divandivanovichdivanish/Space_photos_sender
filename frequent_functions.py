import requests
from urllib.parse import urlsplit
from os.path import splitext
import os
import telegram


def download_image(url, path, file_name, params):
    os.makedirs(path, exist_ok=True)
    img = requests.get(url, params=params)
    img.raise_for_status()
    with open(os.path.join(path, file_name), "wb") as out:
        out.write(img.content)


def get_photo_extension(url):
    path = urlsplit(url)
    extension = splitext(path.path)[1]
    return extension


def publish_photo_to_tg(image_name, telegram_token, chat_id, path):
    bot = telegram.Bot(token=telegram_token)
    with open(os.path.join(path, image_name), 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def get_image_names(path):
    images_info = os.walk(path)
    image_names = []
    for images in images_info:
        image_names = images[2]
    return image_names
