def ReadBonus(params, gameitems):
	bonus = []
	if gameitems[params.lower()].strength != 0:
		bonus.append("{:+} strength".format(gameitems[params.lower()].strength))

	if gameitems[params.lower()].dexterity != 0:
		bonus.append("{:+} dexterity".format(gameitems[params.lower()].dexterity))

	if gameitems[params.lower()].wisdom != 0:
		bonus.append("{:+} wisdom".format(gameitems[params.lower()].wisdom))

	if gameitems[params.lower()].meleed != 0:
		bonus.append("{:+} melee defence".format(gameitems[params.lower()].meleed))

	if gameitems[params.lower()].ranged != 0:
		bonus.append("{:+} ranged defence".format(gameitems[params.lower()].ranged))

	if gameitems[params.lower()].magicd != 0:
		bonus.append("{:+} magic defence".format(gameitems[params.lower()].magicd))	

	bonusstr = "This item has the following bonuses: {}".format(", ".join(bonus))

	return bonusstr

def Look(id, params, players, rooms, gameitems, npcs, beastiary, monsterInstances, mud):
	rm = rooms[players[id].room]																						# store the player's current room
			
	if not params:
		mud.send_message(id, rm.name)																										# if not looking at anything specific
		mud.send_message(id, rm.description)																			# send the player back the description of their current room				
		if rm.roomitems:
			mud.send_message(id, "This room contains: {}".format(", ".join(rm.roomitems)), mud._BOLD, mud._MAGENTA)			# and what is in the room

		playershere = []
		
		for pid, pl in players.items():																					# go through every player in the game					
			if players[pid].room == players[id].room and players[pid].name is not None and pid != id:			# if they're in the same room as the player and they have a name to be shown											
				playershere.append(players[pid].name)																# add their name to the list
		
		if playershere:
			mud.send_message(id, "Adventurers here: {}".format(", ".join(playershere)), mud._BOLD, mud._CYAN)		# send player a message containing the list of players in the room

		if rm.npcs:
			mud.send_message(id, "Citizens here: " + "{}".format(", ".join(rm.npcs)).title(), mud._BOLD, mud._GREEN)

		monstersHere = list()
		for monster in monsterInstances:
			if monsterInstances[monster].room == players[id].room:
				monstersHere.append(monsterInstances[monster].name)

		if len(monstersHere) > 0:
			mud.send_message(id, "Monsters here: " + "{}".format(", ".join(monstersHere)).title(), mud._BOLD, mud._RED)

		if rm.items:
			mud.send_message(id, "On the ground you see: {}".format(", ".join(rm.items)), mud._BOLD, mud._BLUE)
		
		if rm.exits:	
			mud.send_message(id, "Exits are: {}".format(", ".join(rm.exits)), mud._BOLD, mud._YELLOW)			# send player a message containing the list of exits from this room
	
	else:																												# else player wants to examine something in the room
	
		if params.lower() == "me":
			mud.send_message(id, "{} is a(n) {} {}. {} {}".format(players[id].name, players[id].race, players[id].gender, players[id].name, players[id].description))
		
		elif (rm.roomitems) and (params.lower() in rm.roomitems):
			mud.send_message(id, "{}".format(rm.roomitems[params.lower()].description))
			if (rm.roomitems[params.lower()].container) and (rm.roomitems[params.lower()].items):
				mud.send_message(id, "In the {}, you see: {}".format(params.lower(), ", ".join(rm.roomitems[params.lower()].items)), mud._BOLD, mud._BLUE)

		elif (rm.items) and (params.lower() in rm.items):
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))

			if gameitems[params.lower()].__class__.__name__ == "_Weapon" or gameitems[params.lower()].__class__.__name__ == "_Armor":
				mud.send_message(id, ReadBonus(params, gameitems))

		elif (rm.npcs) and (params.lower() in npcs):
			mud.send_message(id, "{}".format(npcs[params.lower()].description))

		elif (params.lower() in beastiary):
			monstersHere = list()
			for monster in monsterInstances:
				if monsterInstances[monster].room == players[id].room:
					monstersHere.append(monsterInstances[monster].name)

			if params.lower() in monstersHere:
				mud.send_message(id, "{}".format(beastiary[params.lower()].description))

			else:
				mud.send_message(id, "You do not see \"{}\" here.".format(params))
			
		elif params.lower() in players[id].inventory:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))

			if gameitems[params.lower()].__class__.__name__ == "_Weapon" or gameitems[params.lower()].__class__.__name__ == "_Armor":
				mud.send_message(id, ReadBonus(params, gameitems))

		elif params.lower() == players[id].weapon1:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))

		elif params.lower() == players[id].weapon2:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].helmet:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].chest:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].legs:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].gloves:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].boots:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].cloak:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].ring:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		elif params.lower() == players[id].necklace:
			mud.send_message(id, "{}".format(gameitems[params.lower()].description))
			mud.send_message(id, ReadBonus(params, gameitems))
		
		else:
			examined = False
			
			for pid, pl in players.items():																# go through all the players in the game
				if players[pid].room == players[id].room:												# if player is in the same room
					if players[pid].name.lower() == params.lower():
						mud.send_message(id, "{} is a(n) {} {}. {} {}".format(players[pid].name, players[pid].race, players[pid].gender, players[pid].name, players[pid].description))
						examined = True
		
			if examined == False:
				mud.send_message(id, "You do not see \"{}\" here.".format(params))
				