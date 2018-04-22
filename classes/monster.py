class _Monster:
	name = ""
	description = ""
	aggressive = False
	hp = 1
	strength = 1
	dexterity = 1
	wisdom = 1
	defence = 1
	meleed = 0
	ranged = 0
	magicd = 0
	drops = None		# TODO change this to a list of _GameItem, perhaps a tuple with drop percentages

	def __init__(self):
		pass