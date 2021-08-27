# pillow is based on PIL, so import Image from PIL
from PIL import Image

# requests handles the http(s) protocol for you, to simplify getting an image from the internet.
import requests


# URL to a specific MEME on Reddit:
url = "https://i.redd.it/4fmgvj6odij71.jpg"


img = Image.open(requests.get(url, stream=True).raw)
img.show()
