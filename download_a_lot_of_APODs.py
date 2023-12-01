import requests
from frequent_functions import download_image, get_photo_extension
from dotenv import load_dotenv
import os


def main():
	nasa_api = os.environ["NASA_API"]
	payload = {"start_date" : "2023-11-01"}
	try:
		response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={nasa_api}", params=payload)
		response.raise_for_status()
		too_many_apods_info = response.json()
		photo_number = 0
		for apod_info in too_many_apods_info:
			photo_number += 1
			extension_of_apod = get_photo_extension(apod_info["url"])
			download_image(apod_info["url"], os.path.join("images", f"apod{photo_number}{extension_of_apod}"))
	except requests.exceptions.HTTPError as e:
		print(f"HTTPError: {e}")



if __name__ == '__main__':
	load_dotenv()
	main()
