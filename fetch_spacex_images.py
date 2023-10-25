import requests
from frequent_functions import download_image, get_photo_extension
import argparse


parser = argparse.ArgumentParser(
	description="Программа скачивает фото с запусков spacex по заданому id."
	)
parser.add_argument("--identifier", "-id", help="Идентификатор полета")
args = parser.parse_args()
if args.identifier != None:
	identifier = args.identifier
else:
	identifier = "last"
response = requests.get(f"https://api.spacexdata.com/v5/launches/{identifier}")
try:
	urls = response.json()["links"]["flickr"]["original"]
	photo_number = 0
	for url in urls:
		photo_number += 1
		extension = get_photo_extension(url)
		download_image(url, f"C:/Users/name/OneDrive/Рабочий стол/dvmn.org/dvmn_API/Lesson4/images/launch{photo_number}{extension}")
except:
	pass
