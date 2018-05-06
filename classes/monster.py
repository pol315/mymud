class _Monster:
	ID = -1
	name = ""
	description = ""
	aggressive = False
	hp = 1
	attack = "melee"
	strength = 1
	dexterity = 1
	wisdom = 1
	meleed = 0
	ranged = 0
	magicd = 0
	drops = None		# TODO change this to a list of _GameItem, perhaps a tuple with drop percentages

	respawn = 100
	death_tick = None

	balance = True
	combat_target = list()
	attack_speed = 20	# number of ticks
	fight_tick = 0

	room = None


	def __init__(self):
		pass