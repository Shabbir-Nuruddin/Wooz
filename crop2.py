import sys
from PIL import Image

def crop():
    img = Image.open('assets/baked3.jpg')
    w, h = img.size
    
    # Bottom half, middle section: X: 30% to 50%, Y: 80% to 100%
    x0, y0 = int(0.3 * w), int(0.8 * h)
    x1, y1 = int(0.5 * w), int(1.0 * h)
    
    cropped = img.crop((x0, y0, x1, y1))
    cropped.save('assets/crop2.jpg')
    print("Crop saved.")

crop()
