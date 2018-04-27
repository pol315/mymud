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
	
def PlacePlayerInGame(id, players, rooms, gameitems, npcs, beastiary, monsterInstances, mud):

	if ((players[id].room is None) or (players[id].room is "")):
		players[id].room = "Hall of Beginnings"

	for pid, pl in players.items():																									# go through all the players in the game
		if pid != id:
			mud.send_message(pid, "{} has entered the game".format(players[id].name))												# send each player a message to tell them about the new player

	mud.send_message(id, "\r\nWelcome to the game, {}. ".format(players[id].name) + "Type 'help' if you get lost. Have fun!")		# send the new player a welcome message			
	mud.send_message(id, "")		
	Look(id, None, players, rooms, gameitems, npcs, beastiary, monsterInstances, mud)																	# send the new player the description of their current room

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

def PlaceMonstersInRooms(rooms, beastiary, monsterInstances):
	monsterIDs = 1

	for room in rooms:
		if rooms[room].monsters:
			for key in rooms[room].monsters:
				currMonster = beastiary[key]
				currMonster.ID = monsterIDs
				currMonster.room = room
				monsterInstances[monsterIDs] = currMonster
				monsterIDs += 1

def CalculateTotalStats(id, players, gameitems, cursor, conn, mud):
	total_strength = players[id].strength	# base stats
	total_dexterity = players[id].dexterity
	total_wisdom = players[id].wisdom
	total_meleed = 0						# defence comes from gear only
	total_ranged = 0
	total_magicd = 0

	if players[id].weapon1:
		total_strength += gameitems[players[id].weapon1].strength
		total_dexterity += gameitems[players[id].weapon1].dexterity
		total_wisdom += gameitems[players[id].weapon1].wisdom
		total_meleed += gameitems[players[id].weapon1].meleed
		total_ranged += gameitems[players[id].weapon1].ranged
		total_magicd += gameitems[players[id].weapon1].magicd

	if players[id].weapon2:
		total_strength += gameitems[players[id].weapon2].strength
		total_dexterity += gameitems[players[id].weapon2].dexterity
		total_wisdom += gameitems[players[id].weapon2].wisdom
		total_meleed += gameitems[players[id].weapon2].meleed
		total_ranged += gameitems[players[id].weapon2].ranged
		total_magicd += gameitems[players[id].weapon2].magicd

	if players[id].helmet:
		total_strength += gameitems[players[id].helmet].strength
		total_dexterity += gameitems[players[id].helmet].dexterity
		total_wisdom += gameitems[players[id].helmet].wisdom
		total_meleed += gameitems[players[id].helmet].meleed
		total_ranged += gameitems[players[id].helmet].ranged
		total_magicd += gameitems[players[id].helmet].magicd

	if players[id].chest:
		total_strength += gameitems[players[id].chest].strength
		total_dexterity += gameitems[players[id].chest].dexterity
		total_wisdom += gameitems[players[id].chest].wisdom
		total_meleed += gameitems[players[id].chest].meleed
		total_ranged += gameitems[players[id].chest].ranged
		total_magicd += gameitems[players[id].chest].magicd

	if players[id].legs:
		total_strength += gameitems[players[id].legs].strength
		total_dexterity += gameitems[players[id].legs].dexterity
		total_wisdom += gameitems[players[id].legs].wisdom
		total_meleed += gameitems[players[id].legs].meleed
		total_ranged += gameitems[players[id].legs].ranged
		total_magicd += gameitems[players[id].legs].magicd

	if players[id].gloves:
		total_strength += gameitems[players[id].gloves].strength
		total_dexterity += gameitems[players[id].gloves].dexterity
		total_wisdom += gameitems[players[id].gloves].wisdom
		total_meleed += gameitems[players[id].gloves].meleed
		total_ranged += gameitems[players[id].gloves].ranged
		total_magicd += gameitems[players[id].gloves].magicd

	if players[id].boots:
		total_strength += gameitems[players[id].boots].strength
		total_dexterity += gameitems[players[id].boots].dexterity
		total_wisdom += gameitems[players[id].boots].wisdom
		total_meleed += gameitems[players[id].boots].meleed
		total_ranged += gameitems[players[id].boots].ranged
		total_magicd += gameitems[players[id].boots].magicd

	if players[id].cloak:
		total_strength += gameitems[players[id].cloak].strength
		total_dexterity += gameitems[players[id].cloak].dexterity
		total_wisdom += gameitems[players[id].cloak].wisdom
		total_meleed += gameitems[players[id].cloak].meleed
		total_ranged += gameitems[players[id].cloak].ranged
		total_magicd += gameitems[players[id].cloak].magicd

	if players[id].necklace:
		total_strength += gameitems[players[id].necklace].strength
		total_dexterity += gameitems[players[id].necklace].dexterity
		total_wisdom += gameitems[players[id].necklace].wisdom
		total_meleed += gameitems[players[id].necklace].meleed
		total_ranged += gameitems[players[id].necklace].ranged
		total_magicd += gameitems[players[id].necklace].magicd

	if players[id].ring:
		total_strength += gameitems[players[id].ring].strength
		total_dexterity += gameitems[players[id].ring].dexterity
		total_wisdom += gameitems[players[id].ring].wisdom
		total_meleed += gameitems[players[id].ring].meleed
		total_ranged += gameitems[players[id].ring].ranged
		total_magicd += gameitems[players[id].ring].magicd

	players[id].totalstr = total_strength
	players[id].totaldex = total_dexterity
	players[id].totalwis = total_wisdom
	players[id].meleed = total_meleed
	players[id].ranged = total_ranged
	players[id].magicd = total_magicd

	cursor.execute("UPDATE player SET totalstr = %s, totaldex = %s, totalwis = %s, meleed = %s, ranged = %s, magicd = %s WHERE username = %s;", (total_strength, total_dexterity, total_wisdom, total_meleed, total_ranged, total_magicd, players[id].name))
	if cursor.rowcount == 1:
		conn.commit()	
	else:
		mud.send_message(id, "Could not update stats.")
		mud.terminate_connection(id)


def CleanUpDeadPlayers(players, gameitems, rooms, monsterInstances, cursor, conn, mud):
	for pl in players:
		if players[pl].hp <= 0:
			mud.send_message(pl, "You have died. Your inventory and what you were wearing have been dropped where you died.")
			mud.send_message(pl, "You have respawned at the Hall of Beginnings.")

			rooms[players[pl].room].items = rooms[players[pl].room].items + players[pl].inventory
			players[pl].inventory = list()

			if players[pl].weapon1:
				rooms[players[pl].room].items.append(players[pl].weapon1)
				players[pl].weapon1 = None

			if players[pl].weapon2:
				rooms[players[pl].room].items.append(players[pl].weapon2)
				players[pl].weapon2 = None

			if players[pl].helmet:
				rooms[players[pl].room].items.append(players[pl].helmet)
				players[pl].helmet = None

			if players[pl].chest:
				rooms[players[pl].room].items.append(players[pl].chest)
				players[pl].chest = None

			if players[pl].legs:
				rooms[players[pl].room].items.append(players[pl].legs)
				players[pl].legs = None

			if players[pl].gloves:
				rooms[players[pl].room].items.append(players[pl].gloves)
				players[pl].gloves = None

			if players[pl].boots:
				rooms[players[pl].room].items.append(players[pl].boots)
				players[pl].boots = None

			if players[pl].cloak:
				rooms[players[pl].room].items.append(players[pl].cloak)
				players[pl].cloak = None

			if players[pl].necklace:
				rooms[players[pl].room].items.append(players[pl].necklace)
				players[pl].necklace = None

			if players[pl].ring:
				rooms[players[pl].room].items.append(players[pl].ring)
				players[pl].ring = None

			CalculateTotalStats(pl, players, gameitems, cursor, conn, mud)

			players[pl].room = "Hall of Beginnings"
			players[pl].hp = 30

			#TODO set player back to their standard max HP

			cursor.execute("UPDATE player SET weapon1 = %s, weapon2 = %s, helmet = %s, chest = %s, legs = %s, gloves = %s, boots = %s, cloak = %s, necklace = %s, ring = %s, last_room = %s WHERE username = %s;", (None, None, None, None, None, None, None, None, None, None, "Hall of Beginnings", players[pl].name))
			if cursor.rowcount == 1:
				conn.commit()	
			else:
				mud.send_message(id, "Could not update stats.")
				mud.terminate_connection(id)

			for monster in monsterInstances:
				if players[pl].name in monsterInstances[monster].combat_target:
					monsterInstances[monster].combat_target.remove(players[pl].name)


			


	


		
