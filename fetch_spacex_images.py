import requests
from frequent_functions import download_image, get_photo_extension
import argparse
import os


def main():
	parser = argparse.ArgumentParser(
		description="Программа скачивает фото с запусков spacex по заданому id."
		)
	parser.add_argument("--identifier", "-id", help="Идентификатор полета")
	args = parser.parse_args()
	if args.identifier != None:
		identifier = args.identifier
	else:
		identifier = "latest"
	try:
		response = requests.get(f"https://api.spacexdata.com/v5/launches/{identifier}")
		response.raise_for_status()
		urls = response.json()["links"]["flickr"]["original"]
		photo_number = 0
		for url in urls:
			photo_number += 1
			extension = get_photo_extension(url)
			download_image(url, os.path.join("images", f"launch{photo_number}{extension}"))
	except requests.exceptions.HTTPError as e:
		print(f"HTTPError: {e}")


if __name__ == '__main__':
	main()
