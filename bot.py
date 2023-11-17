import telegram
import os
from dotenv import load_dotenv
from time import sleep
import argparse
import random


def main():
	load_dotenv()
	telegram_token = os.environ["TG_TOKEN"]
	chat_id = os.environ["TG_CHAT_ID"]
	parser = argparse.ArgumentParser(
		description="Программа запускает телеграмм бота с заданной частотой публикации фото."
		)
	parser.add_argument("--frequency", "-fq", help="С помощью этого аргумента можно регулировать частоту публикации фото (По умолчанию 240 мин). Указывать в минутах.")
	args = parser.parse_args()
	if args.frequency != None:
		frequency = args.frequency
	else:
		frequency = 240
	bot = telegram.Bot(token=telegram_token)
	images_info =  os.walk("images")
	for image in images_info:
		image_names = image[2]
	while True:
		random.shuffle(image_names)
		for image_name in image_names:
			with open(os.path.join("images", image_name), 'rb') as file:
				bot.send_document(chat_id=chat_id, document=file)
			sleep(float(frequency)*60)


if __name__ == '__main__':
	main()