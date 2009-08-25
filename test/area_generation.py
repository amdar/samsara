import data
import misc

class Area:
	"A certain 3 dimensional area the hero can explore."
	def __init__(self, name, desc, size_x, size_y, size_z):
		self.name = name
		self.desc = desc
		self.size_x = size_x
		self.size_y = size_y
		self.size_z = size_z
		self.map = []
		self.map_boundary_x = self.size_x - 1
		self.map_boundary_y = self.size_y - 1
		
		self.__generate_map()
		
	def __generate_map(self):
		"Recursively generates a 3 dimensional map consisting of Tiles"
		# Initialize map
		for fill in range(self.size_x * self.size_y * self.size_z):
			self.map.append(self.__instantiate_tile(data.tile_catalog[0])) # self.__instantiate_tile(data.tile_catalog[0])
		
		# Initialize map generation
		room_info = []
		rooms_to_dig = 16
		corridor_info = []
		corridor_length_max = 8
		corridor_length_min = 4
		
		# Main map generator loop
		first_room_dug = False
		rooms_dug = 0		
		while first_room_dug == False:
			# Dig first room
			room_size_min = 8
			room_size_max = 16
			
			room_size_x = misc.randint(room_size_min, room_size_max)
			room_size_y = misc.randint(room_size_min, room_size_max)
			room_x1 = misc.randint(0, self.map_boundary_x)
			room_y1 = misc.randint(0, self.map_boundary_y)
			room_x2 = room_x1 + room_size_x
			room_y2 = room_y1 + room_size_y
			
			length_of_corridor = self.__place_room_rectangle(room_x1, room_y1, room_x2, room_y2, 0, self.__instantiate_tile(data.tile_catalog[1]), True)
			if length_of_corridor:
				print length_of_corridor
				first_room_dug = True
				rooms_dug += 1
				room_info.append({"x1":room_x1, "y1":room_y1, "x2":room_x2, "y2":room_y2, "length":length_of_corridor})
				
		while rooms_dug < rooms_to_dig:
			# Dig corridor
			while True:
				if misc.randint(0, 1) == 0: # Dig from random room wall
					room_to_dig_from = room_info[misc.randint(0, len(room_info) - 1)]
					wall_to_dig_from = misc.randint(0, 3)
					if wall_to_dig_from == 0:
						corridor_x1 = misc.randint(room_to_dig_from["x1"], room_to_dig_from["x2"])
						corridor_y1 = room_to_dig_from["y1"] - 1
					elif wall_to_dig_from == 1:
						corridor_x1 = room_to_dig_from["x2"] + 1
						corridor_y1 = misc.randint(room_to_dig_from["y1"], room_to_dig_from["y2"])
					elif wall_to_dig_from == 2:
						corridor_x1 = misc.randint(room_to_dig_from["x1"], room_to_dig_from["x2"])
						corridor_y1 = room_to_dig_from["y2"] + 1
					elif wall_to_dig_from == 3:
						corridor_x1 = room_to_dig_from["x1"] - 1
						corridor_y1 = misc.randint(room_to_dig_from["y1"], room_to_dig_from["y2"])
					corridor_x2 = misc.randint(corridor_x1 - corridor_length_max, corridor_x1 + corridor_length_max, corridor_x1 - corridor_length_min, corridor_x1 + corridor_length_min)
					corridor_y2 = misc.randint(corridor_y1 - corridor_length_max, corridor_y1 + corridor_length_max, corridor_y1 - corridor_length_min, corridor_y1 + corridor_length_min)
				else: # Dig from random corridor wall
					break
					if len(corridor_info) == 0:
						break
					corridor_to_dig_from = corridor_info[misc.randint(0, len(corridor_info) - 1)]
					point_in_corridor = misc.randint(0, corridor_to_dig_from['length'])
					(corridor_x1, corridor_y1) = self.__get_coords_within_a_corridor_straight(corridor_to_dig_from['x1'], corridor_to_dig_from['y1'], corridor_to_dig_from['x2'], corridor_to_dig_from['y2'], point_in_corridor)
					corridor_x2 = misc.randint(corridor_x1 - corridor_length_max, corridor_x1 + corridor_length_max, corridor_x1 - corridor_length_min, corridor_x1 + corridor_length_min)
					corridor_y2 = misc.randint(corridor_y1 - corridor_length_max, corridor_y1 + corridor_length_max, corridor_y1 - corridor_length_min, corridor_y1 + corridor_length_min)
					p1 = (corridor_x1 + misc.randint(-1, 1), corridor_y1 + misc.randint(-1, 1))
					p2 = (corridor_x2 + misc.randint(-1, 1), corridor_y2 + misc.randint(-1, 1))
				#if self.__place_corridor_curvy((corridor_x1, corridor_y1), (corridor_x1, corridor_y1), (corridor_x2, corridor_y2), (corridor_x2, corridor_y2), 0, None, True):
				#if self.__place_corridor_curvy((corridor_x1, corridor_y1), (corridor_x1, corridor_y1), (corridor_x2, corridor_y2), (corridor_x2, corridor_y2), 0, self.__instantiate_tile(data.tile_catalog[1]), True):
				if self.__place_corridor_straight(corridor_x1, corridor_y1, corridor_x2, corridor_y2, 0, None, True, True):
					corridor_delta_x = corridor_x2 - corridor_x1
					corridor_delta_y = corridor_y2 - corridor_y1
					
					room_size_x = misc.randint(room_size_min, room_size_max)
					room_size_y = misc.randint(room_size_min, room_size_max)
					if abs(corridor_delta_x) > abs(corridor_delta_y): # Horizontal
						if corridor_x2 > corridor_x1: # Right
							# pass # New Room Right
							room_x1 = corridor_x2 + 1
							room_y1 = corridor_y2 - misc.randint(0, room_size_y)
							room_x2 = room_x1 + room_size_x
							room_y2 = room_y1 + room_size_y
						else: # Left
							room_x1 = corridor_x2 - 1
							room_y1 = corridor_y2 - misc.randint(0, room_size_y)
							room_x2 = room_x1 - room_size_x
							room_y2 = room_y1 + room_size_y
					else: # Vertical
						if corridor_y2 < corridor_y1: # Bottom
							room_x1 = corridor_x2 - misc.randint(0, room_size_x)
							room_y1 = corridor_y2 - 1
							room_x2 = room_x1 + room_size_x
							room_y2 = room_y1 - room_size_y
						else: # Top
							room_x1 = corridor_x2 - misc.randint(0, room_size_x)
							room_y1 = corridor_y2 + 1
							room_x2 = room_x1 + room_size_x
							room_y2 = room_y1 + room_size_y
					
					if self.__place_room_rectangle(room_x1, room_y1, room_x2, room_y2, 0, self.__instantiate_tile(data.tile_catalog[1]), True):
						rooms_dug += 1
						length_of_corridor = self.__place_corridor_straight(corridor_x1, corridor_y1, corridor_x2, corridor_y2, 0, self.__instantiate_tile(data.tile_catalog[1]))
						corridor_info.append({"x1":corridor_x1, "y1":corridor_y1, "x2":corridor_x2, "y2":corridor_y2, "length":length_of_corridor})
						if room_x1 > room_x2:
							(room_x1, room_x2) = (room_x2, room_x1)
						if room_y1 > room_y2:
							(room_y1, room_y2) = (room_y2, room_y1)  
						room_info.append({"x1":room_x1, "y1":room_y1, "x2":room_x2, "y2":room_y2})
						break
						
				for x in range(0, self.size_x):
					self.__place_tile(x, 0, 0, self.__instantiate_tile(data.tile_catalog[2]))
					self.__place_tile(x, self.size_y - 1, 0, self.__instantiate_tile(data.tile_catalog[2]))
				for y in range(0, self.size_y):
					self.__place_tile(0, y, 0, self.__instantiate_tile(data.tile_catalog[2]))
					self.__place_tile(self.size_x - 1, y, 0, self.__instantiate_tile(data.tile_catalog[2]))
					
		a = self.__place_corridor_curvy((10, 1), (50, 5), (5, 15), (20, 20), 0, None, True) == True
		print a
		if a == True:
			self.__place_corridor_curvy((10, 1), (50, 5), (5, 15), (20, 20), 0, self.__instantiate_tile(data.tile_catalog[2]))
		#self.__place_corridor_curvy(20, 15, 60, 30, 25, 40, 50, 15, self.__instantiate_tile(data.tile_catalog[1]), False)
		#self.__place_room_rectangle(0, 0, 12, 12, 0, self.__instantiate_tile(data.tile_catalog[1]))
		#if self.__place_corridor_curvy((10, 10), (20, 10), (30, 30), (10, 30), 0, self.__instantiate_tile(data.tile_catalog[1]), True) == True:
			#self.__place_corridor_curvy((10, 10), (20, 10), (30, 30), (10, 30), 0, self.__instantiate_tile(data.tile_catalog[1]), False)
				
	def __instantiate_tile(self, tile_catalog_entry):
		"Instantiate a single tile based on data from a tile catalog entry"
		return Tile(tile_catalog_entry["name"], tile_catalog_entry["desc"], tile_catalog_entry["char"], tile_catalog_entry["is_solid"])
	
	def __place_tile(self, x, y, z, tile, checkForNonSolidity = False):
		"puts a single tile on the map"
		if x >= 0 and x < self.size_x and y >= 0 and y < self.size_y and z >= 0 and z < self.size_z:
			if checkForNonSolidity == True and self.get_map_tile(x, y, z).is_solid == True:
				return False
			else:
				self.map[x + (y * self.size_x) + (z * self.size_x * self.size_y)] = tile
				
	def __place_room_rectangle(self, x1, y1, x2, y2, z, tile, checkForNonSolidity = False):
		"puts a rectangle room on the map"
		# Invert coordinates if necessary
		if x1 > x2:
			(x1, x2) = (x2, x1)
		if y1 > y2:
			(y1, y2) = (y2, y1)
		
		# Fail if the coordinates do not fit within map 
		if x1 < 0 or x2 >= self.size_x or y1 < 0 or y2 >= self.size_y:
			return False
		
		# Fail if a space where the new room will be has already been dug out
		if checkForNonSolidity == True:
			for y in range(y1 - 1, y2 + 2):
				for x in range(x1 - 1, x2 + 2):
					try:
						if self.get_map_tile(x, y, z).is_solid == False:
							return False
					except:
						pass
					
		# Dig out the room
		for y in range(y1, y2 + 1):
			for x in range(x1, x2 + 1):
				self.__place_tile(x, y, z, tile)
		return True
	
	def __place_corridor_straight(self, x1, y1, x2, y2, z, tile, check_for_non_solidity = False, do_not_dig = False):
		tiles_to_dig = []
		delta_x = x2 - x1
		delta_y = y2 - y1
		
		#self.__put_tile(x1, y1, z, tile)
		tiles_to_dig.append({"x":x1, "y":y1})
		if abs(delta_x) > abs(delta_y):
			m = float(delta_y) / float(delta_x)
			b = float(y1 - m * x1)
			if delta_x < 0:
				delta_x = -1
			else:
				delta_x = 1
			while x1 != x2:
				x1 += delta_x
				tiles_to_dig.append({"x":x1, "y":int(round((m * x1) + b))})
		else:
			if delta_y != 0:
				m = float(delta_x) / float(delta_y)
				b = float(x1 - m * y1)
				if delta_y < 0:
					delta_y = -1
				else:
					delta_y = 1
				while y1 != y2:
					y1 += delta_y
					tiles_to_dig.append({"x":int(round((m * y1) + b)), "y":y1})
		if check_for_non_solidity == True:
			for check in range(len(tiles_to_dig)):
				try:
					if self.get_map_tile(tiles_to_dig[check]["x"], tiles_to_dig[check]["y"], z).is_solid == False:
						return False
					if self.get_map_tile(tiles_to_dig[check]["x"] + delta_x, tiles_to_dig[check]["y"], z).is_solid == False:
						return False
					if self.get_map_tile(tiles_to_dig[check]["x"], tiles_to_dig[check]["y"] + delta_y, z).is_solid == False:
						return False
					if self.get_map_tile(tiles_to_dig[check]["x"] + delta_x, tiles_to_dig[check]["y"] + delta_y, z).is_solid == False:
						return False
				except:
					return False
		length_of_corridor = len(tiles_to_dig)
		if do_not_dig == False:
			for dig in range(length_of_corridor):
				self.__place_tile(tiles_to_dig[dig]["x"], tiles_to_dig[dig]["y"], z, tile)
		return length_of_corridor
	
	def __place_corridor_curvy(self, P1, P2, P3, P4, z, tile, check_for_non_solidity = False, level = 1, level_max = 5):
		print level
		
		if level == level_max:
			x1, y1 = P1
			x2, y2 = P4
			if check_for_non_solidity == False:
				self.__place_corridor_straight(x1, y1, x2, y2, 0, tile)
				return True
			else:
				if self.__place_corridor_straight(x1, y1, x2, y2, 0, None, True, True) == False:
					print "A False"
					return False
				else:
					print "B True"
					return True
		else:
			L1 = P1
			L2 = misc.midpoint(P1, P2)
			H  = misc.midpoint(P2, P3)
			R3 = misc.midpoint(P3, P4)
			R4 = P4
			L3 = misc.midpoint(L2, H)
			R2 = misc.midpoint(R3, H)
			L4 = misc.midpoint(L3, R2)
			R1 = L4
			if check_for_non_solidity == False:
				self.__place_corridor_curvy(L1, L2, L3, L4, z, tile, False, level + 1)
				self.__place_corridor_curvy(R1, R2, R3, R4, z, tile, False, level + 1)
			else:
				self.__place_corridor_curvy(L1, L2, L3, L4, z, tile, True, level + 1)
				self.__place_corridor_curvy(R1, R2, R3, R4, z, tile, True, level + 1)
		return True
		
	def get_map_tile(self, x, y, z):
		"Gets the Tile instance of a specific location on the map"
		try:
			if x < 0 or x >= self.size_x or y < 0 or y >= self.size_y:
				value = None
			else:
				value = self.map[x + (y * self.size_x) + (z * self.size_x * self.size_y)]
		except:
			value = False
			
		return value
	
	def get_map(self, x1, y1, x2, y2, z):
		"Gets the Tile instance of a specific location on the map"
		value = []
		try:
			for y in range(y1, y2):
				for x in range(x1, x2):
					value.append(self.map[x + y * self.size_y])
		except:
			value = False
			
		return value

class Tile:
	"A cubic unit of space"
	def __init__(self, name, desc, char, is_solid = False):
		self.name = name
		self.desc = desc
		self.char = char
		self.is_solid = is_solid
		