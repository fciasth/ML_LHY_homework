from PIL import Image

im = Image.open('westbrook.jpg')
pix = im.load()
width = im.size[0]
height =im.size[1]

newim = Image.new("RGB",(width,height))
for x in range(width):
    for y in range(height):
        r,g,b = pix[x,y]
        newim.putpixel((x,y),(r//2,g//2,b//2))

newim.save('Q2.jpg','jpeg')


