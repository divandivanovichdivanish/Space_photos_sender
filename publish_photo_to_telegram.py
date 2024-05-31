import os
from dotenv import load_dotenv
import argparse
import random
from frequent_functions import publish_photo_to_tg, get_image_names


def main():
    load_dotenv()
    telegram_token = os.environ["TG_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser(
        description="Программа публикует указанное фото в телеграм канал."
        )
    parser.add_argument("--photo_name", "-phn", help="С помощью этого аргумента можно выбрать фото для публикации. Если не указано публикует случайное.")
    parser.add_argument("--path", "-pt", default="images", help="Задает путь к папке с фото.")
    args = parser.parse_args()
    path = args.path
    photo_name = args.photo_name
    image_names = get_image_names(path)
    if photo_name is not None:
        publish_photo_to_tg(photo_name, telegram_token, chat_id, path)
    else:
        random.shuffle(image_names)
        publish_photo_to_tg(image_names[0], telegram_token, chat_id, path)


if __name__ == '__main__':
    main()
