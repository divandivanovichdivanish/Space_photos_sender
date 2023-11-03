import requests
from frequent_functions import download_image, get_photo_extension
from dotenv import load_dotenv
import os


load_dotenv()
nasa_api = os.environ["NASA_API"]
request = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={nasa_api}&start_date=2023-09-01")
too_many_apods_info = request.json()
photo_number = 0
for apod_info in too_many_apods_info:
	photo_number += 1
	extension_of_apod = get_photo_extension(apod_info["url"])
	download_image(apod_info["url"], f"C:/Users/name/OneDrive/Рабочий стол/dvmn.org/dvmn_API/Lesson4/Space_photos_sender/images/apod{photo_number}{extension_of_apod}")
