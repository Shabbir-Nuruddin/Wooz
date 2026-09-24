import sys
from PIL import Image

def crop_neon():
    img = Image.open('assets/baked_ryft.jpg')
    w, h = img.size
    
    # X: 16% to 25%, Y: 50% to 66%
    x0, y0 = int(0.16 * w), int(0.50 * h)
    x1, y1 = int(0.25 * w), int(0.66 * h)
    
    cropped = img.crop((x0, y0, x1, y1))
    cropped.save('assets/crop_neon.jpg')
    print("Neon crop saved.")

crop_neon()
