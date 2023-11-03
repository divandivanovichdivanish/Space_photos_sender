import telegram
import os
from dotenv import load_dotenv
from time import sleep
import argparse
import random


load_dotenv()
telegram_token = os.environ["TG_TOKEN"]
parser = argparse.ArgumentParser(
	description="Программа апускает телеграмм бота с заданой частотой публикации фото."
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
	print(image_names)
	for image_name in image_names:
		bot.send_document(chat_id="@beautifulphotosofspace", document=open(f'images/{image_name}', 'rb'))
		sleep(float(frequency)*60)
