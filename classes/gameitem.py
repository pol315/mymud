class _GameItem:
	name = ""
	description = ""
	unique = False
	sellprice = 0
	weight = 0.0

	def __init__(self):
		pass

class _Weapon(_GameItem):
	hands = 1
	attack = "melee"
	strength = 0
	dexterity = 0
	wisdom = 0
	defence = 0
	meleed = 0
	ranged = 0
	magicd = 0

	def __init__(self):
		pass

class _Armor(_GameItem):
	slot = "chest"
	strength = 0
	dexterity = 0
	wisdom = 0
	defence = 0
	meleed = 0
	ranged = 0
	magicd = 0

	def __init__(self):
		pass