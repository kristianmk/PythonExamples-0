# pillow is based on PIL, so import Image from PIL
from PIL import Image

# requests handles the http(s) protocol for you, to simplify getting an image f$
import requests


# URL to a specific MEME on Reddit:
url = "https://i.redd.it/4fmgvj6odij71.jpg"

with Image.open(requests.get(url, stream=True).raw) as img:
  img.show()
