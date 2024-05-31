import requests
from frequent_functions import download_image, get_photo_extension
from dotenv import load_dotenv
import os
import argparse


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Программа скачивает фото с запусков spacex по заданному id."
        )
    parser.add_argument("--path", "-pt", default="images", help="Задает путь к папке с фото.")
    args = parser.parse_args()
    path = args.path
    payload = {
        "start_date": "2024-03-01",
        "api_key": os.environ["NASA_API"]
    }
    error = False
    try:
        response = requests.get(f"https://api.nasa.gov/planetary/apod", params=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Неверный токен")
        error = True
    except requests.exceptions.ConnectionError:
        print("Такой страницы не существует")
        error = True
    if not error:
        too_many_apods_info = response.json()
        apod_num = 0
        for apod_info in too_many_apods_info:
            if apod_info["media_type"] == "image":
                apod_num += 1
                extension_of_apod = get_photo_extension(apod_info["url"])
                download_image(apod_info["url"], path, f"apod{apod_num}{extension_of_apod}", None)


if __name__ == '__main__':
    main()
