from classes.utilities		import CalculateTotalStats
from classes.utilities		import AdvertiseToRoom

def Equip(id, params, players, gameitems, cursor, conn, mud):

	if (params.lower() in gameitems) and (params.lower() in players[id].inventory): # the item exists and the player owns it
		if (gameitems[params.lower()].__class__.__name__ == "_Weapon") or (gameitems[params.lower()].__class__.__name__ == "_Armor"):
			if gameitems[params.lower()].__class__.__name__ == "_Weapon":
				if (gameitems[params.lower()].hands == 2) and (players[id].weapon1 == None) and (players[id].weapon2 == None):
					players[id].weapon1 = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} equips a {} with both hands.".format(players[id].name, params.lower()), "You equip the {} in both hands.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET weapon1 = %s WHERE username = %s;", (params.lower(), players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				elif (gameitems[params.lower()].hands == 1) and ((players[id].weapon1 == None) or (players[id].weapon2 == None)):
					if players[id].weapon1 == None:
						players[id].weapon1 = params.lower()
						players[id].inventory.remove(params.lower())
						AdvertiseToRoom(id, "{} equips a {} in their main hand.".format(players[id].name, params.lower()), "You equip the {} in your main hand.".format(params.lower()), players, mud)
						
						cursor.execute("UPDATE player SET weapon1 = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
						if cursor.rowcount == 1:
							conn.commit()	
						else:
							mud.send_message(id, "Could not update equipment.")
							mud.terminate_connection(id)

						CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
						
					else:
						players[id].weapon2 = params.lower()
						players[id].inventory.remove(params.lower())
						AdvertiseToRoom(id, "{} equips a {} in their off hand.".format(players[id].name, params.lower()), "You equip the {} in your off hand.".format(params.lower()), players, mud)
						
						cursor.execute("UPDATE player SET weapon2 = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
						if cursor.rowcount == 1:
							conn.commit()	
						else:
							mud.send_message(id, "Could not update equipment.")
							mud.terminate_connection(id)

						CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
						
				else:
					mud.send_message(id, "Your hands are already full.")								
			
			elif gameitems[params.lower()].__class__.__name__ == "_Armor":
				if (gameitems[params.lower()].slot == "chest") and (players[id].chest == None):
					players[id].chest = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} equips a {} on their chest.".format(players[id].name, params.lower()), "You equip the {} on your chest.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET chest = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				elif (gameitems[params.lower()].slot == "helmet") and (players[id].helmet == None):
					players[id].helmet = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} equips a {} on their head.".format(players[id].name, params.lower()), "You equip the {} on your head.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET helmet = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
			
				elif (gameitems[params.lower()].slot == "legs") and (players[id].legs == None):
					players[id].legs = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} equips a {} on their legs.".format(players[id].name, params.lower()), "You equip the {} on your legs.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET legs = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				elif (gameitems[params.lower()].slot == "gloves") and (players[id].gloves == None):
					players[id].gloves = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} equips some {} on their hands.".format(players[id].name, params.lower()), "You equip the {} on your hands.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET gloves = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				elif (gameitems[params.lower()].slot == "boots") and (players[id].boots == None):
					players[id].boots = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} equips some {} on their feet.".format(players[id].name, params.lower()), "You equip the {} on your feet.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET boots = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				elif (gameitems[params.lower()].slot == "cloak") and (players[id].cloak == None):
					players[id].cloak = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} equips a {} on their back.".format(players[id].name, params.lower()), "You equip the {} on your back.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET cloak = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				elif (gameitems[params.lower()].slot == "necklace") and (players[id].necklace == None):
					players[id].necklace = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} wears a {} around their neck.".format(players[id].name, params.lower()), "You wear the {} around your neck.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET necklace = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				elif (gameitems[params.lower()].slot == "ring") and (players[id].ring == None):
					players[id].ring = params.lower()
					players[id].inventory.remove(params.lower())
					AdvertiseToRoom(id, "{} wears a {} on their finger.".format(players[id].name, params.lower()), "You wear the {} on your finger.".format(params.lower()), players, mud)
					
					cursor.execute("UPDATE player SET ring = %s, inventory = %s WHERE username = %s;", (params.lower(), players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "Could not update equipment.")
						mud.terminate_connection(id)

					CalculateTotalStats(id, players, gameitems, cursor, conn, mud)
					
				else:
					mud.send_message(id, "You're already wearing a {}.".format(gameitems[params.lower()].slot))				
		
		else:
			mud.send_message(id, "You cannot equip that.")
	
	else:
		mud.send_message(id, "You do not have a \"{}\"".format(params.lower()))