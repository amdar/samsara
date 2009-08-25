import random

# VERY BUGGY!!!
def randint(min, max, exclude_from = False, exclude_to = False):
	if min > max:
		(min, max) = (max, min)
	if exclude_from != False and exclude_to != False:
		if exclude_from > exclude_to:
			(exclude_from, exclude_to) = (exclude_to, exclude_from)
		if random.randint(0, 1):
			value = random.randint(min, exclude_from - 1)
		else:
			value = random.randint(exclude_to + 1, max)
	else:
		value = random.randint(min, max)
	return value

def midpoint(point1, point2):
	(x1, y1) = point1
	(x2, y2) = point2
	return ((x1 + x2) / 2, (y1 + y2) / 2)
	
