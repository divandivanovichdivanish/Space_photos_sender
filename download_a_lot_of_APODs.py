import requests
from frequent_functions import download_image, get_photo_extension
from dotenv import load_dotenv
import os


def main():
	payload = {
		"start_date" : "2023-11-01",
		"api_key" : os.environ["NASA_API"]
	}
	try:
		response = requests.get(f"https://api.nasa.gov/planetary/apod", params=payload)
		response.raise_for_status()
	except requests.exceptions.HTTPError:
		print("Неверный токен")
	except DoesNotExist:
		print("Такой страницы не существует")
	too_many_apods_info = response.json()
	for apod_num, apod_info in enumerate(too_many_apods_info):
		extension_of_apod = get_photo_extension(apod_info["url"])
		if not os.path.exists('images'):
			os.makedirs('images')
		download_image(apod_info["url"], os.path.join("images", f"apod{apod_num + 1}{extension_of_apod}"), None)



if __name__ == '__main__':
	main()
