import requests
from frequent_functions import download_image, get_photo_extension
import argparse
import os
from dotenv import load_dotenv


def download_photos(response):
	urls = response.json()["links"]["flickr"]["original"]
	for url_num, url in enumerate(urls, start=1):
		extension = get_photo_extension(url)
		download_image(url, os.path.join(path, f"launch{url_num}{extension}"), None)

def main():
	load_dotenv()
	parser = argparse.ArgumentParser(
		description="Программа скачивает фото с запусков spacex по заданному id."
		)
	parser.add_argument("--identifier", "-id", default="latest", help="Идентификатор полета")
	parser.add_argument("--path", "-pt", default="images", help="Задает путь к папке с фото.")
	args = parser.parse_args()
	path = args.path
	identifier = args.identifier
	try:
		response = requests.get(f"https://api.spacexdata.com/v5/launches/{identifier}")
		response.raise_for_status()
		download_photos(response)
	except requests.exceptions.ConnectionError:
		print("Нет такой страницы")
	except AttributeError:
        print("Отсутствуют ссылки на фотографии")


if __name__ == '__main__':
	main()
