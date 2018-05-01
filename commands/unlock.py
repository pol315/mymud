from classes.utilities	import AdvertiseToRoom

def Unlock(id, params, players, rooms, cursor, conn, mud):
	if params:
		if (rooms[players[id].room].roomitems) and (params.lower() in rooms[players[id].room].roomitems):
			if (rooms[players[id].room].roomitems[params.lower()].locked):
				if (rooms[players[id].room].roomitems[params.lower()].key in players[id].inventory):
					players[id].inventory.remove(rooms[players[id].room].roomitems[params.lower()].key)

					AdvertiseToRoom(id, "{} unlocks the {} and takes the goods inside.".format(players[id].name, params.lower()), "You unlock the {}. Your key turns to dust.".format(params.lower()), players, mud)
					for i in rooms[players[id].room].roomitems[params.lower()].items:
						players[id].inventory.append(i)
						mud.send_message(id, "You take a {} from the {}.".format(i, params.lower()), mud._BOLD, mud._GREEN)

					cursor.execute("UPDATE player SET inventory = %s WHERE username = %s;", (players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
						mud.terminate_connection(id)

				else:
					mud.send_message(id, "You don't seem to have the correct key.")	
			
			else:
				mud.send_message(id, "You can't unlock that.")	
		
		else:
			mud.send_message(id, "You don't see that here.")	

	else:
		mud.send_message(id, "Unlock what?")