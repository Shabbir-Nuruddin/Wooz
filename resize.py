import sys
from PIL import Image

def resize():
    img = Image.open('assets/baked3.jpg')
    resized = img.resize((1024, 1024))
    resized.save('assets/resized.jpg')
    print("Resized.")

resize()
