import pytesseract
from PIL import Image

text = pytesseract.image_to_string(Image.open("data/Screenshot 2026-03-16 094240.png"), lang='vie') # remove lang='vie' if it's english

print(text)