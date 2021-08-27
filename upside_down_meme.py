# pillow is based on PIL, so import Image from PIL
from PIL import Image


# Upside down meme file (make sure to run from a directory containing this file!):
fileName = "upside-down-meme.png"

with Image.open(fileName) as img:
  img.show()
