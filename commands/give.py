def Give(id, params, players, gameitems, cursor, conn, mud):

	if (params) and (" to " in params):
		item = params.lower().split(" to ")[0]
		target = params.lower().split(" to ")[1]

		itemalias = ParseAlias(id, item, players, rooms, None, "inventory")
		targetalias = ParseAlias(id, target, players, rooms, None, "npcs")


		if (itemalias) and (itemalias in players[id].inventory):
			if (targetalias) and (rooms[players[id].room].npcs) and (targetalias in rooms[players[id].room].npcs):
				

			else:
				mud.send_message(id, "That person isn't here.")	
		
		else:
			mud.send_message(id, "You don't have that item.")

	else:
		mud.send_message(id, "Give what to whom?")

