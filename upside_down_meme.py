# pillow is based on PIL, so import Image from PIL
from PIL import Image

# requests handles the http(s) protocol for you, to simplify getting an image
# from the internet.
import requests


# Upside down meme file (make sure to run from a directory containing this file!):
fileName = "upside-down-meme.png"

with Image.open(fileName) as img:
  img.show()
