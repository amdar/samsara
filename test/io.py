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
