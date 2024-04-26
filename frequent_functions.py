import requests
from urllib.parse import urlsplit, unquote
from os.path import splitext
import os
import telegram


def download_image(url, path, params):
	os.makedirs("images", exist_ok=True)
	img = requests.get(url, params=params)
	img.raise_for_status()
	with open(path, "wb") as out:
		out.write(img.content)

def get_photo_extension(url):
	path = urlsplit(url)
	extension = splitext(path.path)[1]
	return extension

def publish_photo_to_tg(image_name, telegram_token, chat_id):
	bot = telegram.Bot(token=telegram_token)
	with open(os.path.join("images", image_name), 'rb') as file:
		bot.send_document(chat_id=chat_id, document=file)

def get_image_names():
	images_info =  os.walk("images")
	for images in images_info:
		image_names = images[2]
	return image_names