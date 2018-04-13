def Take(id, params, players, rooms, gameitems, cursor, conn, mud):
	if params:
		
		if " from " not in params.lower(): 	# the player is taking an item directly from the ground of the current room
			if params.lower() in rooms[players[id].room]["items"]:		# the item has to be in the room
				del rooms[players[id].room]["items"][params.lower()]
				players[id].inventory.append(params.lower())
				mud.send_message(id, "You pick up: {}".format(params.lower()))
				
				#TODO database commit
				
			else:
				mud.send_message(id, "You don't see that here.")
				
			
		else: 						# the player is taking an item from a container that exists in the current room
			pass
			
	else:
		mud.send_message(id, "Take what?")