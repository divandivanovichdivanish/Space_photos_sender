import requests
from urllib.parse import urlsplit, unquote
from os.path import splitext


def download_image(url, path):
	img = requests.get(url)
	out = open(path, "wb")
	out.write(img.content)
	out.close()

def get_photo_extension(url):
	path = urlsplit(url)
	extension = splitext(path.path)[1]
	return extension
