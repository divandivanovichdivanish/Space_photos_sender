import requests
from frequent_functions import download_image, get_photo_extension
import argparse
import os

def main():
	parser = argparse.ArgumentParser(
		description="Программа скачивает фото с запусков spacex по заданному id."
		)
	parser.add_argument("--identifier", "-id", default="latest", help="Идентификатор полета")
	args = parser.parse_args()
	identifier = args.identifier
	try:
		response = requests.get(f"https://api.spacexdata.com/v5/launches/{identifier}")
		response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		print(f"HTTPError: {e}")
	urls = response.json()["links"]["flickr"]["original"]
	for url_num, url in enumerate(urls):
		extension = get_photo_extension(url)
		download_image(url, os.path.join("images", f"launch{url_num}{extension}"))


if __name__ == '__main__':
	main()
