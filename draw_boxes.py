import sys
from PIL import Image, ImageDraw

def draw_test_boxes():
    img = Image.open('assets/baked3.jpg')
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    
    boxes = [
        # Example format: (x_start, y_start, x_end, y_end) in percentages 0-100
        # Tote bag "W O O Z" (bottom middle-ish)
        (43, 90, 46, 95),
        
        # Green poster WZ (mid left)
        (17, 51, 24, 57),
        (17, 59, 24, 67),
        
        # Small "wooz" text on beige poster
        (9, 61, 15, 63),
        
        # Splatter shirts (W O O Z) - Top right quadrant
        (56, 43, 61, 47),
        (69, 43, 73, 47),
        (82, 43, 86, 47)
    ]
    
    for box in boxes:
        x0, y0, x1, y1 = box
        px0, py0 = int(x0/100.0 * w), int(y0/100.0 * h)
        px1, py1 = int(x1/100.0 * w), int(y1/100.0 * h)
        
        draw.rectangle([px0, py0, px1, py1], outline="red", width=20)
        
    img.save('assets/test.jpg', quality=50)

draw_test_boxes()
print("Done")
