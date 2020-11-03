from PIL import Image

img = Image.open("Screenshot-from-2018-10-16-09-31-31.png")
img = img.convert("RGB")

datas = img.getdata()

new_image_data = []
for item in datas:
    # change all white (also shades of whites) pixels to yellow
    if item[0] in list(range(0, 192)):
        new_image_data.append((255, 255, 255))
    else:
        new_image_data.append(item)

        
# update image data
img.putdata(new_image_data)

# save new image
img.save("test_image_altered_background.jpg")

# show image in preview
img.show()
