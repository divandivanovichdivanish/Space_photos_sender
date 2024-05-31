import os
from dotenv import load_dotenv
from time import sleep
import argparse
import random
from telegram.error import NetworkError
from frequent_functions import publish_photo_to_tg, get_image_names


def main():
    load_dotenv()
    telegram_token = os.environ["TG_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser(
        description="Программа запускает телеграмм бота с заданной частотой публикации фото."
        )
    parser.add_argument("--frequency", "-fq", default=240, help="С помощью этого аргумента можно регулировать частоту публикации фото (По умолчанию 240 мин). Указывать в минутах.", type=int)
    parser.add_argument("--path", "-pt", default="images", help="Задает путь к папке с фото.")
    args = parser.parse_args()
    frequency = args.frequency * 60
    path = args.path
    image_names = get_image_names(path)
    while True:
        random.shuffle(image_names)
        if not image_names:
            print("Папка images пуста или отсутствует.")
            break
        for image_name in image_names:
            while True:
                try:
                    publish_photo_to_tg(image_name, telegram_token, chat_id, path)
                    break
                except NetworkError as e:
                    print("NetworkError: ", e, "try again after 5 seconds")
                    sleep(5)
            sleep(frequency)


if __name__ == '__main__':
    main()
