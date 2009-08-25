import sys

import io
import data

if __name__ == "__main__":
	try:
		#io = io.Curses()
		io = io.Pygame()
		
		hero_x = 40
		hero_y = 40
		while(True):
			# input
			input = io.input_get()
			
			velocity_x = 0
			velocity_y = 0
			if input == io.KEY_RIGHT:
				velocity_x = 1
			elif input == io.KEY_LEFT:
				velocity_x = -1
			if input == io.KEY_DOWN:
				velocity_y = 1
			elif input == io.KEY_UP:
				velocity_y = -1
			
			if input == io.KEY_q:
				io.deinit()
				exit()
				
			# 
			#if not data.areas[0].get_map_tile(hero_x + velocity_x, hero_y + velocity_y, 0).is_solid:
			hero_x += velocity_x		
			hero_y += velocity_y
			
			# camera
			console_size_y, console_size_x = io.getmaxyx()
			console_size_x_half = (console_size_x + 1) / 2
			console_size_y_half = (console_size_y + 1) / 2
			if hero_x < console_size_x_half:
				camera_x = 0
			elif hero_x > data.areas[0].size_x - console_size_x_half:
				if data.areas[0].size_x > console_size_x:
					camera_x = data.areas[0].size_x - console_size_x
				else:
					camera_x = 0
			else:
				camera_x = hero_x - console_size_x_half
			if hero_y < console_size_y_half:
				camera_y = 0
			elif hero_y > data.areas[0].size_y - console_size_y_half:
				if data.areas[0].size_y > console_size_y:
					camera_y = data.areas[0].size_y - console_size_y
				else:
					camera_y = 0
			else:
				camera_y = hero_y - console_size_y_half
			
			# render map
			for y in range(0, console_size_y):
				for x in range(0, console_size_x):
					try:
						io.print_char(x, y, data.areas[0].get_map_tile(camera_x + x, camera_y + y, 0).char)
					except:
						pass
			
			# render characters
			if hero_x < (console_size_x / 2) or camera_x == 0:
				print_hero_x = hero_x
			elif hero_x > data.areas[0].size_x - (console_size_x / 2):
				print_hero_x = hero_x - (data.areas[0].size_x - console_size_x)
			else:
				print_hero_x = (console_size_x / 2)
			if hero_y < (console_size_y / 2) or camera_y == 0:
				print_hero_y = hero_y
			elif hero_y > data.areas[0].size_y - (console_size_y / 2):
				print_hero_y = hero_y - (data.areas[0].size_y - console_size_y)
			else:
				print_hero_y = (console_size_y / 2)
			io.print_char(print_hero_x, print_hero_y, "@")
			
			io.print_string(0, 0, "x: " + str(camera_x))
			io.print_string(0, 1, "y: " + str(camera_y))
			io.print_string(0, 2, "width: " + str(console_size_x))
			io.print_string(0, 3, "height: " + str(console_size_y))
			io.print_string(0, 5, "hero_x: " + str(hero_x))
			io.print_string(0, 6, "hero_y: " + str(hero_y))
			
			#io.print_char(0, 0, str(input))
			
			io.refresh()
			
		io.refresh()
		io.input_clear()
		print "oompf"
	except:
		io.deinit()
		print "Unexpected error:", sys.exc_info()[0]
