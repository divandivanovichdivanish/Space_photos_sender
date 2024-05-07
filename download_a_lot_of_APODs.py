import requests
from frequent_functions import download_image, get_photo_extension
from dotenv import load_dotenv
import os


def main():
	load_dotenv()
	payload = {
		"start_date" : "2024-03-01",
		"api_key" : os.environ["NASA_API"]
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
		for apod_num, apod_info in enumerate(too_many_apods_info, start=1):
			extension_of_apod = get_photo_extension(apod_info["url"])
			download_image(apod_info["url"], os.path.join("images", f"apod{apod_num}{extension_of_apod}"), None)




if __name__ == '__main__':
	main()
