from PIL import Image, ImageDraw
import math

imgx = 800
imgy = 600
img = Image.new("RGB", (imgx, imgy))
draw = ImageDraw.Draw(img)
stpoint = (float(imgx) / 2, float(imgy) * 0.95)
	
def radToDegree(rad):
	return rad * 180 / math.pi
	
def degreeToRad(deg):
	return deg / 180.0 * math.pi
	
def angleFromPoint(startpoint, length, angle):
	addx = math.sin(degreeToRad(angle)) * length
	addy = math.cos(degreeToRad(angle)) * length
	newx = startpoint[0] + addx
	newy = startpoint[1] + addy
	return (newx, newy)
		
def tree(startpoint, lastlength, absolutangle, depth, numaeste=7, addangle=50):
	gval = int(255*depth/7.0)
	col = (0, gval, 0)
	if depth == 0:
		return
	depth -= 1
	
	for i in range(1, numaeste + 1):
		newlength = lastlength * 0.6 - lastlength * 0.6 * i / numaeste
		middlepoint = angleFromPoint(startpoint, lastlength * i / numaeste, absolutangle)
		absangler = absolutangle - addangle
		absanglel = absolutangle + addangle
		endr = angleFromPoint(middlepoint, newlength, absangler)
		endl = angleFromPoint(middlepoint, newlength, absanglel)
		draw.line((middlepoint, endr), fill=col)
		draw.line((middlepoint, endl), fill=col)
		tree(middlepoint, newlength, absangler, depth)
		tree(middlepoint, newlength, absanglel, depth)

depth = 4
draw.line((stpoint, angleFromPoint(stpoint, imgy * 0.9, 180)), fill=(0, int(255 * (depth + 1) / 7.0), 0))
tree(stpoint, imgy * 0.9, 180, depth)
img.show()
