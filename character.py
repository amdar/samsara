class Soul:
	"Core identity of all beings"
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc
		
class Character(Soul):
	"How a being is perceived by others"
	def __init__(self, name, desc, limbs):
		Soul.__init__(self, name, desc)
		limbs = []
		# TODO Personality, etc come here
		
class Limb:
	"All types of body parts"
	def __init__(self, name, desc, health):
		self.name = name
		self.desc = desc
		self.health_maximum = health
		self.health_current = health
