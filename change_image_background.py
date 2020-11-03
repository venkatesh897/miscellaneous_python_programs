#Program to change background color of image from white to black
from PIL import Image

img = Image.open("Screenshot-from-2018-10-16-09-31-31.png")
img = img.convert("RGB")

datas = img.getdata()

new_image_data = []
for item in datas:
    # change all white (also shades of whites) pixels to yellow
    if item[0] in list(range(190, 255)):
        new_image_data.append((0, 0, 0))
    else:
        new_image_data.append(item)
        
img.putdata(new_image_data)

img.save("test_image_altered_background.jpg")

img.show()
