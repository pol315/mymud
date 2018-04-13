def Inventory(id, params, players, mud):

	if players[id].inventory:
		mud.send_message(id, "You are currently holding:\r\n{}".format("\r\n".join(players[id].inventory)))
		
	else:
		mud.send_message(id, "You aren't currently holding anything.")