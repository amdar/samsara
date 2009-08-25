import Image
import ImageDraw

SIZE=128
image = Image.new("RGB", (SIZE, SIZE))
d = ImageDraw.Draw(image)

def midpoint((x1, y1), (x2, y2)):
	return ((x1 + x2) / 2, (y1 + y2) / 2)

MAX_LEVEL = 100
def draw_curve(P1, P2, P3, P4, level=1):
	if level == MAX_LEVEL:
		d.line((P1, P4))
	else:
		L1 = P1
		L2 = midpoint(P1, P2)
		H  = midpoint(P2, P3)
		R3 = midpoint(P3, P4)
		R4 = P4
		L3 = midpoint(L2, H)
		R2 = midpoint(R3, H)
		L4 = midpoint(L3, R2)
		R1 = L4
		draw_curve(L1, L2, L3, L4, level+1)
		draw_curve(R1, R2, R3, R4, level+1)

draw_curve((10,10),(100,100),(100,10),(100,100))

image.save(r"./DeCasteljau.png", "PNG")

print "ok."