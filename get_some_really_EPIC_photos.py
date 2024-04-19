import requests
from frequent_functions import download_image
from dotenv import load_dotenv
import os
from datetime import datetime


def main():
	load_dotenv()
	nasa_api = os.environ["NASA_API"]
	payload = {"api_key" : nasa_api}
	error = False
	try:
		response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images", params=payload)
		response.raise_for_status()
	except requests.exceptions.HTTPError:
		print("Неверный токен")
		error = True
	except requests.exceptions.ConnectionError:
		print("Такой страницы не существует") 
		error = True
	if not error:
		for photo_info in response.json():
			response_date = photo_info["date"]
			date = datetime.fromisoformat(response_date)
			formatted_date = date.strftime("%Y/%m/%d")
			identifier = photo_info["image"]
			try:
				download_image(f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{identifier}.png", os.path.join("images", f"{identifier}.png"), payload)
			except requests.exceptions.HTTPError:
				print("Неверный токен")
			except requests.exceptions.ConnectionError:
				print("Такой страницы не существует")


if __name__ == '__main__':
	main()
