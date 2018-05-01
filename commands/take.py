from classes.utilities	import AdvertiseToRoom
from classes.utilities	import ParseAlias

def Take(id, params, players, rooms, gameitems, cursor, conn, mud):
	
	if params:		
		if " from " not in params.lower(): 	# the player is taking an item directly from the ground of the current room
			takealias = ParseAlias(id, params.lower(), players, rooms, None, "items")
			if takealias in rooms[players[id].room].items:		# the item has to be in the room			
					rooms[players[id].room].items.remove(takealias)
					players[id].inventory.append(takealias)
					AdvertiseToRoom(id, "{} picks up a {} from the ground.".format(players[id].name, takealias), "You pick up a {} from the ground.".format(takealias), players, mud)
					
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

			itemalias = ParseAlias(id, item, players, rooms, None, "containeritems")
			containeralias = ParseAlias(id, container, players, rooms, None, "roomitems")
			
			if containeralias in rooms[players[id].room].roomitems:
				if rooms[players[id].room].roomitems[containeralias].container:
					if itemalias in rooms[players[id].room].roomitems[containeralias].items:
						if itemalias in gameitems:
							if rooms[players[id].room].roomitems[containeralias].infinite is False:
								rooms[players[id].room].roomitems[containeralias].items.remove(itemalias)
								
							players[id].inventory.append(itemalias)
							AdvertiseToRoom(id, "{} takes a {} from the {}.".format(players[id].name, itemalias, containeralias), "You take a {} from the {}.".format(itemalias, containeralias), players, mud)				
							
							cursor.execute("UPDATE player SET inventory = %s WHERE username = %s;", (players[id].inventory, players[id].name))
							if cursor.rowcount == 1:
								conn.commit()	
							else:
								mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
								mud.terminate_connection(id)
								
						else:
							mud.send_message(id, "\"{}\" does not exist here.".format(itemalias))
					
					else:
						mud.send_message(id, "\"{}\" is not in the container.".format(itemalias))
					
				else:
					mud.send_message(id, "\"{}\" is not a container.".format(containeralias))
					
			else:
				mud.send_message(id, "You don't see \"{}\" here.".format(containeralias))
			
	else:
		mud.send_message(id, "Take what?")