import requests
from frequent_functions import download_image
from dotenv import load_dotenv
import os
from datetime import datetime
import argparse


def format_date(response_date):
    date = datetime.fromisoformat(response_date)
    formatted_date = date.strftime("%Y/%m/%d")
    return formatted_date


def download_photo(photo_info, payload, path):
    formatted_date = format_date(photo_info["date"])
    identifier = photo_info["image"]
    download_image(
        f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{identifier}.png",
        path, 
        f"{identifier}.png",
        payload
        )


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Программа скачивает фото с запусков spacex по заданному id."
    )
    parser.add_argument("--path", "-pt", default="images", help="Задает путь к папке с фото.")
    args = parser.parse_args()
    path = args.path
    nasa_api = os.environ["NASA_API"]
    payload = {"api_key": nasa_api}
    try:
        response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images", params=payload)
        response.raise_for_status()
        for photo_info in response.json():
            download_photo(photo_info, payload, path)
    except requests.exceptions.HTTPError:
        print("Неверный токен")
    except requests.exceptions.ConnectionError:
        print("Такой страницы не существует")


if __name__ == '__main__':
    main()
