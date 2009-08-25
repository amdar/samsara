def plot_line(point1, point2):
	"""Brensenham line algorithm"""
	(x1, y1) = point1
	(x2, y2) = point2
	
	coords = []
	steep = 0
	
	delta_x = abs(x2 - x1)
	if (x2 - x1) > 0:
		step_x = 1
	else:
		step_x = -1
	delta_y = abs(y2 - y1)
	if (y2 - y1) > 0:
		step_y = 1
	else:
		step_y = -1
	if delta_y > delta_x:
		steep = 1
		x1, y1 = y1, x1
		delta_x, delta_y = delta_y, delta_x
		step_x, step_y = step_y, step_x
	delta = (2 * delta_y) - delta_x
	
	for i in range(0, delta_x):
		if steep:
			coords.extend([(y1, x1)])
		else:
			coords.extend([(x1, y1)])
		while delta >= 0:
			y1 = y1 + step_y
			delta = delta - (2 * delta_x)
		x1 = x1 + step_x
		delta = delta + (2 * delta_y)
	coords.extend([(x2, y2)])
	
	coords = sorted(set(coords), key=coords.index) # TODO: Should make this unnecessary
	
	return coords
	
def plot_line_curvy(point1, point2, point3, point4, level = 1, level_max = 5):
	"""de Casteljau algorithm"""
	coords = []
	
	if level == level_max:
		x1, y1 = point1
		x2, y2 = point4
		coords.extend(plot_line((x1, y1), (x2, y2)))
	else:
		L1 = point1
		L2 = midpoint(point1, point2)
		H  = midpoint(point2, point3)
		R3 = midpoint(point3, point4)
		R4 = point4
		L3 = midpoint(L2, H)
		R2 = midpoint(R3, H)
		L4 = midpoint(L3, R2)
		R1 = L4
		coords.extend(plot_line_curvy(L1, L2, L3, L4, level + 1))
		coords.extend(plot_line_curvy(R1, R2, R3, R4, level + 1))
		
	return coords
	
def plot_rectangle(point1, point2):
	"""plot rectangle"""
	coords = []
	
	x1, y1 = point1
	x2, y2 = point2
	if x1 > x2:
		x1, x2 = x2, x1
	if y1 > y2:
		y1, y2 = y2, y1
		
	for plot_y in range(y1, y2):
		for plot_x in range(x1, x2):
			coords.extend([(plot_x, plot_y)])
			
	return coords
	
def plot_polygon(points, filled=False):
	"""plot polygon"""

	coords = []
	
	for index in range(0, len(points) - 1):
		coords.extend(plot_line(points[index], points[index + 1]))
	coords.extend(plot_line(points[len(points) - 1], points[0]))
	
	if filled == True:
		min_x, min_y = points[1]
		max_x, max_y = points[1]
		
		for point in points:
			x, y = point
			if x < min_x:
				min_x = x
			elif x > max_x:
				max_x = x
			if y < min_y:
				min_y = y
			elif y > max_y:
				max_y = y
			
		plot_on = []
		for x in range(min_x - 1, max_x + 1):
			plot_on.append(False)
		for y in range(min_y - 1, max_y + 1):
			for x in range(min_x - 1, max_x + 1):
				if plot_on[x] == True:
					coords.append((x, y))
				if (x, y + 1) in coords:
					plot_on[x] = False
				else:
					plot_on[x] = True
					
	coords = sorted(set(coords), key=coords.index)
	
	return coords
	
def midpoint(point1, point2):
	(x1, y1) = point1
	(x2, y2) = point2
	return ((x1 + x2) / 2, (y1 + y2) / 2)
	
