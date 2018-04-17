def Look(id, params, players, rooms, gameitems, mud):
	rm = rooms[players[id].room]																						# store the player's current room
			
	if not params:																										# if not looking at anything specific
		mud.send_message(id, rm["description"])																			# send the player back the description of their current room				
		mud.send_message(id, "This room contains: {}".format(", ".join(rm["furni"])), mud._BOLD, mud._MAGENTA)			# and what is in the room

		playershere = []
		
		for pid, pl in players.items():																					# go through every player in the game					
			if players[pid].room == players[id].room and players[pid].name is not None and pid != id:			# if they're in the same room as the player and they have a name to be shown											
				playershere.append(players[pid].name)																# add their name to the list
		
		if playershere:
			mud.send_message(id, "Players here: {}".format(", ".join(playershere)), mud._BOLD, mud._CYAN)		# send player a message containing the list of players in the room

		itemshere = []	
			
		for key in rm["items"]:
			itemshere.append(key)
			
		if itemshere:
			mud.send_message(id, "On the ground you see: {}".format(", ".join(itemshere)), mud._BOLD, mud._BLUE)
			
		mud.send_message(id, "Exits are: {}".format(", ".join(rm["exits"])), mud._BOLD, mud._YELLOW)			# send player a message containing the list of exits from this room
	
	else:																												# else player wants to examine something in the room
	
		if params.lower() == "me":
			mud.send_message(id, "{} is a(n) {} {}. {} {}".format(players[id].name, players[id].race, players[id].gender, players[id].name, players[id].description))
		
		elif params.lower() in rm["furni"]:
			mud.send_message(id, "{}".format(rm["furni"][params.lower()]["description"]))
			if rm["furni"][params.lower()]["items"]:
				mud.send_message(id, "In the {}, you see: {}".format(params.lower(), ", ".join(rm["furni"][params.lower()]["items"])), mud._BOLD, mud._BLUE)

		elif params.lower() in rm["items"]:
			mud.send_message(id, "{}".format(gameitems[params.lower()]["description"]))
			
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