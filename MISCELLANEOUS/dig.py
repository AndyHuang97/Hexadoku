from PIL import Image

im = Image.open("Blood.png")

# im.convert(mode="L").show()
# there are 4 bands in this image,
# get pixels from all bands(0-R, 1-G, 2-B, 3-A)
# getdata() returns a list of tuples of the pixels
pixelsR = list(im.getdata(band=0))
pixelsG = list(im.getdata(band=1))
pixelsB = list(im.getdata(band=2))
pixelsA = list(im.getdata(band=3))


newpixels = list()
# print the size of the list of pixels, and size (hxw) of the image
print(len(pixelsR), im.size)
# for every pixel of the image, set bands RGB to 0 and only band A to R+200
# +200 is to make the image darker for a better eye recognition
for i in range(len(pixelsR)) :
    G = pixelsG[i]
    B = pixelsB[i]
    R = pixelsR[i]
    A = pixelsA[i]
    newpixels.append((0,0,0,R+200))

# creates a new Image instance
imR = Image.new(im.mode, im.size)
# puts the list of tuples of pixels in the imR object
imR.putdata(newpixels)
imR.show()

# width, height = im.size
# pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
