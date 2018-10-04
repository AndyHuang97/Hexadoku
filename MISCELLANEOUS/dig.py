from PIL import Image

im = Image.open("Blood.png")

# im.convert(mode="L").show()

pixelsR = list(im.getdata(band=0))
pixelsG = list(im.getdata(band=1))
pixelsB = list(im.getdata(band=2))
pixelsA = list(im.getdata(band=3))

newpixels = list()
print(len(pixelsR), im.size)
for i in range(len(pixelsR)) :
    G = pixelsG[i]
    B = pixelsB[i]
    R = pixelsR[i]
    A = pixelsA[i]
    newpixels.append((0,0,0,R+200))
# print(pixels)
# [0]*len(pixelsA)
imR = Image.new(im.mode, im.size)
imR.putdata(newpixels)
imR.show()

# width, height = im.size
# pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
