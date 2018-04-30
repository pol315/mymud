class _RoomItem:
	name = ""
	description = ""
	container = False
	infinite = False	# does this container hold infinite of what it contains? this menas you can't put items IN the container too
	open = False
	locked = False
	key = ""
	items = list() 		# list of _GameItem

	def __init__(self):
		pass