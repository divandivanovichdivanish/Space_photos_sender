import os
from dotenv import load_dotenv
import argparse
import random
from frequent_functions import publish_photo_to_tg

def main():
	load_dotenv()
	telegram_token = os.environ["TG_TOKEN"]
	chat_id = os.environ["TG_CHAT_ID"]
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
		publish_photo_to_tg(photo_name, telegram_token, chat_id)
	else:
		random.shuffle(image_names)
		publish_photo_to_tg(image_names[0], telegram_token, chat_id)



if __name__ == '__main__':
	main()
