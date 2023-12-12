import telegram
import os
from dotenv import load_dotenv
import argparse
import random

def main():
	telegram_token = os.environ["TG_TOKEN"]
	chat_id = os.environ["TG_CHAT_ID"]
	bot = telegram.Bot(token=telegram_token)
	images_info =  os.walk("images")
	for images in images_info:
		image_names = images[2]
	parser = argparse.ArgumentParser(
		description="Программа публикует указанное фото в телеграм канал."
		)
	parser.add_argument("--photo_name", "-phn", help="С помощью этого аргумента можно выбрать фото для публикации. Если не указано публикует случайное.")
	args = parser.parse_args()
	photo_name = args.photo_name
	if photo_name is not None:
		with open(os.path.join("images", photo_name), 'rb') as file:
			bot.send_document(chat_id=chat_id, document=file)
	else:
		random.shuffle(image_names)
		with open(os.path.join("images", f'{image_names[0]}'), 'rb') as file:
			bot.send_document(chat_id=chat_id, document=file)


if __name__ == '__main__':
	load_dotenv()
	main()
