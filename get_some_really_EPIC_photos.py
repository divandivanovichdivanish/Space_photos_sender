import requests
from frequent_functions import download_image
from dotenv import load_dotenv
import os


def main():
	load_dotenv()
	nasa_api = os.environ["NASA_API"]
	payload = {"api_key" : nasa_api}
	try:
		response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images", params=payload)
		response.raise_for_status()
	except requests.exceptions.HTTPError:
		print("Неверный токен")
	except DoesNotExist:
		print("Такой страницы не существует")
	for photo_info in response.json():
		response_date = photo_info["date"]
		date = response_date.split()
		split_date = date[0].split("-")
		identifier = photo_info["image"]
		download_image(f"https://api.nasa.gov/EPIC/archive/natural/{split_date[0]}/{split_date[1]}/{split_date[2]}/png/{identifier}.png", os.path.join("images", f"{identifier}.png"), payload)


if __name__ == '__main__':
	main()
