from PIL import Image, ImageDraw

def test():
    img = Image.open('assets/crop2.jpg')
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # Relative to this crop
    x0, y0 = int(0.68 * w), int(0.50 * h)
    x1, y1 = int(0.81 * w), int(0.77 * h)
    
    draw.rectangle([x0, y0, x1, y1], outline='red', width=5)
    img.save('assets/crop2_test.jpg')
    print("Test saved.")

test()
