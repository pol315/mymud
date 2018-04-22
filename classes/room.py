class _Room:
	name = ""
	description = ""
	roomitems = list()		# of _RoomItem
	items = list()			# of _GameItem
	npcs = list()			# of _NPC
	monsters = list()		# of _Monster
	exits = list()

	def __init__(self):
		pass