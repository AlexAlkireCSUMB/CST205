#
#       Title: CST 205 Project 1 Abstract: Filters a set of images to
#       find a combined background image. Author: Alex Alkire
#
#

from PIL import Image
import statistics
import time
import sys
from multiprocessing import Pool

start = time.time()
image = [0] * 9
try :
	image[1] = Image.open("Project1Images/1.png")
except FileNotFoundError:
	print("ERROR: File 1.png not found.")
	sys.exit()
height = image[1].height
width = image[1].width

for i in range (2,9):
	try:
		image[i] = Image.open("Project1Images/%d.png" % i)
	except FileNotFoundError:
		print("ERROR: File",i,".png not found.",sep='')
		sys.exit()
	# All dimensions must match to compare images.
	if (image[i].width != width):
		print("ERROR: Width mismatch. Image 1.png width = ", width, " Image ",i, ".png width = ", image[i].width, sep='')
		sys.exit()
	if (image[i].height != height):
		print("ERROR: Height mismatch. Image 1.png height = ", height, " Image ", i, ".png height = ", image[i].height, sep='' )
		sys.exit()

rgb = [(0,0,0)]*9
newImage = Image.new("RGB", (width,height))

def filterPixel(x, y):
	for z in range (1,9):
		rgb[z] = image[z].getpixel((x, y))
	newImage.putpixel((x,y), statistics.median(rgb))

for x in range (0, width):
#   Some failed attempts to multiprocess.
#   p = Pool(width+1)
#   p.map(funcA, (x, range(0,height)))
	for y in range (0, height):
		filterPixel(x,y)
		#Could improve this by doing a custom median by sorting rgb values as they are added.

newImage.show()
end = time.time()-start
print("Done %d seconds." % end)
