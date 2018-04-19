def Take(id, params, players, rooms, gameitems, cursor, conn, mud):
	
	#TODO FIX DATABASE STUFFS
	
	if params:		
		if " from " not in params.lower(): 	# the player is taking an item directly from the ground of the current room
			if params.lower() in rooms[players[id].room]["items"]:		# the item has to be in the room
				if (gameitems[params.lower()]["unique"] == "true") and (params.lower() in players[id].inventory):
					mud.send_message(id, "You may only have one of that item at a time.")
				
				else:
					rooms[players[id].room]["items"].remove(params.lower())
					players[id].inventory.append(params.lower())
					mud.send_message(id, "You pick up: {}".format(params.lower()))
					
					cursor.execute("UPDATE player SET inventory = %s WHERE username = %s;", (players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
						mud.terminate_connection(id)
				
			else:
				mud.send_message(id, "You don't see that here.")
				
			
		else: 						# the player is taking an item from a container that exists in the current room
			container = params.lower().split(" from ")[1]
			item = params.lower().split(" from ")[0]
			
			if container in rooms[players[id].room]["furni"]:
				if rooms[players[id].room]["furni"][container]["container"] == "true":
					if item in rooms[players[id].room]["furni"][container]["items"]:
						if item in gameitems:
							if (gameitems[item]["unique"] == "true") and (item in players[id].inventory):
								mud.send_message(id, "You may only have one of that item at a time.")
							
							elif gameitems[item]["unique"] == "true":
								players[id].inventory.append(item)
								mud.send_message(id, "You take a {} from the {}.".format(item, container))

							else:	
								rooms[players[id].room]["furni"][container]["items"].remove(item)
								players[id].inventory.append(item)
								mud.send_message(id, "You take a {} from the {}.".format(item, container))
							
							
							
							cursor.execute("UPDATE player SET inventory = %s WHERE username = %s;", (players[id].inventory, players[id].name))
							if cursor.rowcount == 1:
								conn.commit()	
							else:
								mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
								mud.terminate_connection(id)
								
						else:
							mud.send_message(id, "\"{}\" does not exist here.".format(item))
					
					else:
						mud.send_message(id, "\"{}\" is not in the container.".format(item))
					
				else:
					mud.send_message(id, "\"{}\" is not a container.".format(container))
					
			else:
				mud.send_message(id, "You don't see \"{}\" here.".format(container))
			
	else:
		mud.send_message(id, "Take what?")