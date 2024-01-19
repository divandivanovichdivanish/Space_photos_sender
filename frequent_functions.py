import requests
from urllib.parse import urlsplit, unquote
from os.path import splitext
import os
import telegram


def download_image(url, path, params):	
	if not os.path.exists("images"):
		os.mkdir("images")
	try:
		img = requests.get(url, params=params)
		with open(path, "wb") as out:
			out.write(img.content)
	except requests.exceptions.HTTPError:
		print("Неверный токен")
	except DoesNotExist:
		print("Такой страницы не существует")

def get_photo_extension(url):
	path = urlsplit(url)
	extension = splitext(path.path)[1]
	return extension

def publish_photo_to_tg(image_name):
	telegram_token = os.environ["TG_TOKEN"]
	chat_id = os.environ["TG_CHAT_ID"]
	bot = telegram.Bot(token=telegram_token)
	with open(os.path.join("images", image_name), 'rb') as file:
		bot.send_document(chat_id=chat_id, document=file)
