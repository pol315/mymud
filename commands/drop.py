def Drop(id, params, players, rooms, cursor, conn, mud):
	if params.lower() in players[id].inventory:
		players[id].inventory.remove(params.lower())
		rooms[players[id].room].items.append(params.lower())
		
		cursor.execute("UPDATE player SET inventory = %s WHERE username = %s;", (players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)
		
		
		mud.send_message(id, "You drop a {}.".format(params.lower()))
	
	else:
		mud.send_message(id, "You do not have a {}.".format(params.lower()))
	