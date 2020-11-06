import PIL
from PIL import Image

def grayscale(picture):
    res=PIL.Image.new(picture.mode, picture.size)
    width, height = picture.size

    for i in range(0, width):
        for j in range(0, height):
            pixel=picture.getpixel((i,j))
            avg=int((pixel[0]+pixel[1]+pixel[2])/3)
            res.putpixel((i,j),(avg,avg,avg))
    res.show()

image_fp = r'Screenshot-from-2018-10-16-09-31-31.png'
image = Image.open(image_fp)
grayscale(image)
