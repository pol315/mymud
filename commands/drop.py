def Drop(id, params, players, rooms, cursor, conn, mud):
	if params.lower() in players[id].inventory:
		players[id].inventory.remove(params.lower())
		rooms[players[id].room]["items"].append(params.lower())
		
		#TODO database commit
		
		
		mud.send_message(id, "You drop: {}".format(params.lower()))
	
	else:
		mud.send_message(id, "You do not have \"{}\"".format(params.lower()))
	