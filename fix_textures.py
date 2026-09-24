import sys
from PIL import Image, ImageDraw
import numpy as np

def fix_texture():
    img = Image.open('assets/baked3.jpg')
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    
    # Regions to paint over (x0, y0, x1, y1) in percentages
    regions = [
        # Tote bag "WOOZ" text - vertical text on the white bag
        (44.3, 90.2, 45.4, 95.0),
        
        # Green poster top "WZ"
        (17.2, 53.5, 20.8, 57.0),
        
        # Green poster bottom "WZ"
        (17.2, 63.5, 20.8, 67.0),
        
        # Beige poster "wooz"
        (11.0, 62.3, 13.0, 63.2),
        
        # Shirt splat 1 WOOZ text
        (57.5, 44.5, 59.5, 45.5),
        
        # Shirt splat 2 WOOZ text
        (70.0, 44.5, 72.0, 45.5),
        
        # Shirt splat 3 WOOZ text
        (83.0, 44.5, 85.0, 45.5),
        
        # There's another "wooz" on the green bag/box in the bottom right of the green section?
        # Actually let's just do these.
    ]
    
    for box in regions:
        x0, y0, x1, y1 = box
        px0, py0 = int(x0/100.0 * w), int(y0/100.0 * h)
        px1, py1 = int(x1/100.0 * w), int(y1/100.0 * h)
        
        # Sample the background color from just outside the top-left of the box
        # We'll take an average of a 5x5 patch above the box to be safe
        patch = []
        for i in range(px0, px0 + 10):
            for j in range(py0 - 10, py0):
                if 0 <= i < w and 0 <= j < h:
                    patch.append(img.getpixel((i, j)))
        
        if patch:
            avg_color = tuple(np.median(patch, axis=0).astype(int))
            # draw the filled rectangle with the background color
            draw.rectangle([px0, py0, px1, py1], fill=avg_color)
            
    img.save('assets/baked3.jpg', quality=90)
    print("Texture updated.")

fix_texture()
