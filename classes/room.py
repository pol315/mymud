class _Room:
	name = ""
	description = ""
	roomitems = None		# list of _RoomItem
	items = list()			# list of _GameItem
	npcs = list()			# list of _NPC
	monsters = list()		# list of _Monster
	exits = None

	def __init__(self):
		pass