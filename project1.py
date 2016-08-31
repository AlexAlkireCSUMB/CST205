from PIL import Image
import statistics
import time
from multiprocessing import Pool

start = time.time()
image = [0] * 9

image[1] = Image.open("Project1Images/1.png")
height = image[1].height
width = image[1].width

for i in range (2,9):
    image[i] = Image.open("Project1Images/%d.png" % i)
    # All dimensions must match to compare images.
    if (image[i].width != width):
        print("INVALID WIDTH")
        exit
    if (image[i].height != height):
        print("INVALID HEIGHT")
        exit
rgb = [(0,0,0)]*9
newImage = Image.new("RGB", (width,height))

def funcA(x, y):
    for z in range (1,9):
        rgb[z] = image[z].getpixel((x, y))
    newImage.putpixel((x,y), statistics.median(rgb))

for x in range (0, width):
#    p = Pool(width+1)
#   p.map(funcA, (x, range(0,height)))
    for y in range (0, height):
        funcA(x,y)
        #Could improve this by doing a custom median by sorting rgb values as they are added.

newImage.show()
end = time.time()-start
print("Done %d seconds." % end)
