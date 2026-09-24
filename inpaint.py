import sys
import cv2
import numpy as np

def inpaint_texture():
    img = cv2.imread('assets/baked3.jpg')
    h, w = img.shape[:2]
    
    # Create an empty mask
    mask = np.zeros((h, w), dtype=np.uint8)
    
    regions = [
        # Main logo on the wall
        (43.4, 89.8, 46.5, 95.6),
        
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
    ]
    
    for box in regions:
        x0, y0, x1, y1 = box
        px0, py0 = int(x0/100.0 * w), int(y0/100.0 * h)
        px1, py1 = int(x1/100.0 * w), int(y1/100.0 * h)
        
        # Draw a white rectangle on the mask
        cv2.rectangle(mask, (px0, py0), (px1, py1), 255, -1)
        
    print("Inpainting... this may take a moment for an 8k image.")
    # Inpaint using Telea algorithm
    inpainted = cv2.inpaint(img, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    
    cv2.imwrite('assets/baked3.jpg', inpainted, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    print("Texture updated.")

inpaint_texture()
