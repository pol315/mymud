def Look(id, params, players, rooms, gameitems, npcs, monsters, mud):
	rm = rooms[players[id].room]																						# store the player's current room
			
	if not params:																										# if not looking at anything specific
		mud.send_message(id, rm["description"])																			# send the player back the description of their current room				
		mud.send_message(id, "This room contains: {}".format(", ".join(rm["roomitems"])), mud._BOLD, mud._MAGENTA)			# and what is in the room

		playershere = []
		
		for pid, pl in players.items():																					# go through every player in the game					
			if players[pid].room == players[id].room and players[pid].name is not None and pid != id:			# if they're in the same room as the player and they have a name to be shown											
				playershere.append(players[pid].name)																# add their name to the list
		
		if playershere:
			mud.send_message(id, "Adventurers here: {}".format(", ".join(playershere)), mud._BOLD, mud._CYAN)		# send player a message containing the list of players in the room

		if "npcs" in rm:
			mud.send_message(id, "Citizens here: " + "{}".format(", ".join(rm["npcs"])).title(), mud._BOLD, mud._GREEN)

		if "monsters" in rm:
			mud.send_message(id, "Monsters here: " + "{}".format(", ".join(rm["monsters"])).title(), mud._BOLD, mud._RED)

		if "items" in rm:
			mud.send_message(id, "On the ground you see: {}".format(", ".join(rm["items"])), mud._BOLD, mud._BLUE)
		
		if "exits" in rm:	
			mud.send_message(id, "Exits are: {}".format(", ".join(rm["exits"])), mud._BOLD, mud._YELLOW)			# send player a message containing the list of exits from this room
	
	else:																												# else player wants to examine something in the room
	
		if params.lower() == "me":
			mud.send_message(id, "{} is a(n) {} {}. {} {}".format(players[id].name, players[id].race, players[id].gender, players[id].name, players[id].description))
		
		elif ("roomitems" in rm) and (params.lower() in rm["roomitems"]):
			mud.send_message(id, "{}".format(rm["roomitems"][params.lower()]["description"]))
			if "items" in rm["roomitems"][params.lower()]:
				mud.send_message(id, "In the {}, you see: {}".format(params.lower(), ", ".join(rm["roomitems"][params.lower()]["items"])), mud._BOLD, mud._BLUE)

		elif ("items" in rm) and (params.lower() in rm["items"]):
			mud.send_message(id, "{}".format(gameitems[params.lower()]["description"]))

		elif ("npcs" in rm) and (params.lower() in npcs):
			mud.send_message(id, "{}".format(npcs[params.lower()]["description"]))

		elif ("monsters" in rm) and (params.lower() in monsters):
			mud.send_message(id, "{}".format(monsters[params.lower()]["description"]))
			
		elif params.lower() in players[id].inventory:
			mud.send_message(id, "{}".format(gameitems[params.lower()]["description"]))
		
		else:
			examined = False
			
			for pid, pl in players.items():																# go through all the players in the game
				if players[pid].room == players[id].room:												# if player is in the same room
					if players[pid].name.lower() == params.lower():
						mud.send_message(id, "{} is a(n) {} {}. {} {}".format(players[pid].name, players[pid].race, players[pid].gender, players[pid].name, players[pid].description))
						examined = True
		
			if examined == False:
				mud.send_message(id, "You do not see \"{}\" here.".format(params))
				
	mud.send_message(id, "")