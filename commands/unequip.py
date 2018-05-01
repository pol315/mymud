from classes.utilities		import CalculateTotalStats
from classes.utilities		import AdvertiseToRoom

def Unequip(id, params, players, gameitems, cursor, conn, mud):
	if players[id].chest == params.lower():
		players[id].inventory.append(players[id].chest)
		players[id].chest = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET chest = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	elif players[id].helmet == params.lower():
		players[id].inventory.append(players[id].helmet)
		players[id].helmet = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET helmet = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	elif players[id].legs == params.lower():
		players[id].inventory.append(players[id].legs)
		players[id].legs = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET legs = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	elif players[id].boots == params.lower():
		players[id].inventory.append(players[id].boots)
		players[id].boots = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET boots = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	elif players[id].gloves == params.lower():
		players[id].inventory.append(players[id].gloves)
		players[id].gloves = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET gloves = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	elif players[id].cloak == params.lower():
		players[id].inventory.append(players[id].cloak)
		players[id].cloak = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET cloak = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	elif players[id].necklace == params.lower():
		players[id].inventory.append(players[id].necklace)
		players[id].necklace = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET necklace = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	elif players[id].ring == params.lower():
		players[id].inventory.append(players[id].ring)
		players[id].ring = None
		AdvertiseToRoom(id, "{} unequips a {}.".format(players[id].name, params.lower()), "You unequip the {}.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET ring = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)

	elif players[id].weapon2 == params.lower():							# if offhand is same as mainhand, remove offhand first
		players[id].inventory.append(players[id].weapon2)
		players[id].weapon2 = None
		AdvertiseToRoom(id, "{} unequips a {} from their off hand.".format(players[id].name, params.lower()), "You unequip the {} from your off hand.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET weapon2 = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)

	elif players[id].weapon1 == params.lower():
		players[id].inventory.append(players[id].weapon1)
		players[id].weapon1 = None
		AdvertiseToRoom(id, "{} unequips a {} from their main hand.".format(players[id].name, params.lower()), "You unequip the {} from your main hand.".format(params.lower()), players, mud)
		
		cursor.execute("UPDATE player SET weapon1 = %s, inventory = %s WHERE username = %s;", (None, players[id].inventory, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update equipment.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
	else:
		mud.send_message(id, "You aren't wearing anything with that name.")