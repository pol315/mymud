from commands.look		import Look

from classes.room	 		import _Room
from classes.roomitem 		import _RoomItem
from classes.gameitem 		import _GameItem
from classes.gameitem 		import _Weapon
from classes.gameitem 		import _Armor
from classes.npc	 		import _NPC
from classes.monster 		import _Monster

def MakeProper(message):		
	if ((message[-1] is '.') or (message[-1] is '?') or (message[-1] is '!')):
		pass
	else:
		message = message + "."
		
	return message.capitalize()
	
def PlacePlayerInGame(id, players, rooms, gameitems, npcs, monsters, mud):

	if ((players[id].room is None) or (players[id].room is "")):
		players[id].room = "Hall of Beginnings"

	for pid, pl in players.items():																									# go through all the players in the game
		if pid != id:
			mud.send_message(pid, "{} has entered the game".format(players[id].name))												# send each player a message to tell them about the new player

	mud.send_message(id, "\r\nWelcome to the game, {}. ".format(players[id].name) + "Type 'help' if you get lost. Have fun!")		# send the new player a welcome message			
	mud.send_message(id, "")		
	Look(id, None, players, rooms, gameitems, npcs, monsters, mud)																	# send the new player the description of their current room

def AdvertiseToRoom(id, message, selfmessage, players, mud):
	if selfmessage is not None:
		mud.send_message(id, selfmessage)

	for pid, pl in players.items():														
		if (pid != id) and (players[pid].room == players[id].room):
			mud.send_message(pid, message)

def StringToBool(v):
	return str(v).lower() in ("yes", "true", "t", "1")

def ParseRoomItems(itemsdict):
	roomitems = {}

	for key in itemsdict:
		currItem = _RoomItem()
		currItem.name = key
		currItem.description = itemsdict[key]["description"]

		if "container" in itemsdict[key]:
			currItem.container = StringToBool(itemsdict[key]["container"])

		if "open" in itemsdict[key]:
			currItem.open = StringToBool(itemsdict[key]["open"])

		if "locked" in itemsdict[key]:
			currItem.locked = StringToBool(itemsdict[key]["locked"])

		if "key" in itemsdict[key]:
			currItem.key = itemsdict[key]["key"]

		if "items" in itemsdict[key]:
			currItem.items = itemsdict[key]["items"]

		roomitems[key] = currItem

	return roomitems

def ParseRooms(roomdict):
	rooms = {}

	for key in roomdict:
		currRoom = _Room()
		currRoom.name = key
		currRoom.description = roomdict[key]["description"]
		
		if "roomitems" in roomdict[key]:
			currRoom.roomitems = ParseRoomItems(roomdict[key]["roomitems"])

		if "items" in roomdict[key]:
			currRoom.items = roomdict[key]["items"]

		if "npcs" in roomdict[key]:
			currRoom.npcs = roomdict[key]["npcs"]

		if "monsters" in roomdict[key]:
			currRoom.monsters = roomdict[key]["monsters"]

		if "exits" in roomdict[key]:
			currRoom.exits = roomdict[key]["exits"]

		rooms[key] = currRoom
		
	return rooms

def ParseGameItems(itemsdict):
	gameitems = {}

	for key in itemsdict:
		currItem = None

		if ("type" in itemsdict[key]) and (itemsdict[key]["type"] == "weapon"):
			currItem = _Weapon()
			currItem.hands = itemsdict[key]["hands"]
			currItem.attack = itemsdict[key]["attack"]

			if "stats" in itemsdict[key]:
				if "strength" in itemsdict[key]["stats"]:
					currItem.strength = itemsdict[key]["stats"]["strength"]

				if "dexterity" in itemsdict[key]["stats"]:
					currItem.dexterity = itemsdict[key]["stats"]["dexterity"]

				if "wisdom" in itemsdict[key]["stats"]:
					currItem.wisdom = itemsdict[key]["stats"]["wisdom"]

				if "defence" in itemsdict[key]["stats"]:
					currItem.defence = itemsdict[key]["stats"]["defence"]

				if "meleed" in itemsdict[key]["stats"]:
					currItem.meleed = itemsdict[key]["stats"]["meleed"]

				if "ranged" in itemsdict[key]["stats"]:
					currItem.ranged = itemsdict[key]["stats"]["ranged"]

				if "magicd" in itemsdict[key]["stats"]:
					currItem.magicd = itemsdict[key]["stats"]["magicd"]

		elif ("type" in itemsdict[key]) and (itemsdict[key]["type"] == "armor"):
			currItem = _Armor()
			currItem.slot = itemsdict[key]["slot"]

			if "stats" in itemsdict[key]:
				if "strength" in itemsdict[key]["stats"]:
					currItem.strength = itemsdict[key]["stats"]["strength"]

				if "dexterity" in itemsdict[key]["stats"]:
					currItem.dexterity = itemsdict[key]["stats"]["dexterity"]

				if "wisdom" in itemsdict[key]["stats"]:
					currItem.wisdom = itemsdict[key]["stats"]["wisdom"]

				if "defence" in itemsdict[key]["stats"]:
					currItem.defence = itemsdict[key]["stats"]["defence"]

				if "meleed" in itemsdict[key]["stats"]:
					currItem.meleed = itemsdict[key]["stats"]["meleed"]

				if "ranged" in itemsdict[key]["stats"]:
					currItem.ranged = itemsdict[key]["stats"]["ranged"]

				if "magicd" in itemsdict[key]["stats"]:
					currItem.magicd = itemsdict[key]["stats"]["magicd"]

		else:
			currItem = _GameItem()

		currItem.name = key
		currItem.description = itemsdict[key]["description"]

		if "unique" in itemsdict[key]:
			currItem.unique = StringToBool(itemsdict[key]["unique"])
		
		if "sellprice" in itemsdict[key]:
			currItem.sellprice = itemsdict[key]["sellprice"]

		if "weight" in itemsdict[key]:
			currItem.weight = itemsdict[key]["weight"]

		gameitems[key] = currItem

	return gameitems

def ParseNPCs(npcdict):
	npcs = {}

	for key in npcdict:
		currNPC = _NPC()
		currNPC.name = key
		currNPC.description = npcdict[key]["description"]

		if "response" in npcdict[key]:
			currNPC.response = npcdict[key]["response"]

		if "receives" in npcdict[key]:
			currNPC.receives = npcdict[key]["receives"]

		if "result" in npcdict[key]:
			currNPC.result = npcdict[key]["result"]

		npcs[key] = currNPC

	return npcs

def ParseMonsters(monsterdict):
	monsters = {}

	for key in monsterdict:
		currMonster = _Monster()
		currMonster.name = key
		currMonster.description = monsterdict[key]["description"]

		if "aggressive" in monsterdict[key]:
			currMonster.aggressive = StringToBool(monsterdict[key]["aggressive"])

		if "hp" in monsterdict[key]:
			currMonster.hp = monsterdict[key]["hp"]

		if "attack" in monsterdict[key]:
			currMonster.attack = monsterdict[key]["attack"]

		if "attack_speed" in monsterdict[key]:
			currMonster.attack_speed = monsterdict[key]["attack_speed"]

		if "drops" in monsterdict[key]:
			currMonster.drops = monsterdict[key]["drops"]

		if "stats" in monsterdict[key]:
				if "strength" in monsterdict[key]["stats"]:
					currMonster.strength = monsterdict[key]["stats"]["strength"]

				if "dexterity" in monsterdict[key]["stats"]:
					currMonster.dexterity = monsterdict[key]["stats"]["dexterity"]

				if "wisdom" in monsterdict[key]["stats"]:
					currMonster.wisdom = monsterdict[key]["stats"]["wisdom"]				

				if "meleed" in monsterdict[key]["stats"]:
					currMonster.meleed = monsterdict[key]["stats"]["meleed"]

				if "ranged" in monsterdict[key]["stats"]:
					currMonster.ranged = monsterdict[key]["stats"]["ranged"]

				if "magicd" in monsterdict[key]["stats"]:
					currMonster.magicd = monsterdict[key]["stats"]["magicd"]

		monsters[key] = currMonster

	return monsters

def PlaceMonstersInRooms(rooms, monsters):
	for room in rooms:
		if rooms[room].monsters:
			for key in rooms[room].monsters:
				rooms[room].monsters[key] = monsters[key]

		
