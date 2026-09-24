import sys
from PIL import Image

def crop():
    img = Image.open('assets/baked3.jpg')
    w, h = img.size
    
    # Let's crop from X: 0 to 25%, Y: 50% to 75%
    x0, y0 = int(0.0 * w), int(0.5 * h)
    x1, y1 = int(0.25 * w), int(0.75 * h)
    
    cropped = img.crop((x0, y0, x1, y1))
    cropped.save('assets/crop.jpg')
    print("Crop saved.")

crop()
