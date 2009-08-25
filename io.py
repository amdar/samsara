try:
	import curses
	
	class Curses:
		KEY_DOWN = curses.KEY_DOWN
		KEY_UP = curses.KEY_UP
		KEY_LEFT = curses.KEY_LEFT
		KEY_RIGHT = curses.KEY_RIGHT
		
		def __init__(self):
			try:
				self.screen = curses.initscr()
				curses.noecho()
				curses.cbreak()
				curses.curs_set(0)
				self.screen.keypad(1)
			except:
				self.deinit()
				exit()
			
		def print_char(self, x, y, char, status = None):
			try:
				self.screen.addch(y, x, char)
			except:
				pass
			  
		def print_string(self, x, y, string, status = None):
			try:
				self.screen.addstr(y, x, string)
			except:
				pass
				
		def refresh(self):
			self.screen.refresh()
			
		def input_get(self):
			return self.screen.getch()
			
		def input_clear(self):
			curses.flushinp()
			
		def deinit(self):
			self.screen.keypad(0)
			curses.echo()
			curses.nocbreak()
			curses.endwin()
			
except ImportError:
	pass

try:
	import pygame
	import pygame.locals
	
	class Pygame:
		KEY_DOWN = pygame.locals.K_DOWN
		KEY_UP = pygame.locals.K_UP
		KEY_LEFT = pygame.locals.K_LEFT
		KEY_RIGHT = pygame.locals.K_RIGHT
		KEY_q = pygame.locals.K_q
		
		def __init__(self):
			try:
				pygame.init()
				self.screen = pygame.display.set_mode((640,480))
				pygame.display.set_caption(u"key event")
			except:
				pass
			
		def getmaxyx(self):
			x, y = self.screen.get_size()
			return (y, x)
			
		def print_char(self, x, y, char, status = None):
			self.screen.set_at((x, y), (255, 0, 0))
			  
		def print_string(self, x, y, string, status = None):
			pass
				
		def refresh(self):
			#self.screen.fill((0,0,255))
			pygame.display.update()
			
		def input_get(self):
			return pygame.event.get()
			
		def input_clear(self):
			pass
			
		def deinit(self):
			pass
					
except ImportError:
	pass
	