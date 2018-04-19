def Equip(id, params, players, gameitems, cursor, conn, mud):

	#TODO DATABASE COMMITS

	if (params.lower() in gameitems) and (params.lower() in players[id].inventory): # the item exists and the player owns it
		if (gameitems[params.lower()]["type"] == "weapon") or (gameitems[params.lower()]["type"] == "armor"):
			if gameitems[params.lower()]["type"] == "weapon":
				if (gameitems[params.lower()]["hands"] == 2) and (players[id].weapon1 == None) and (players[id].weapon2 == None):
					players[id].weapon1 = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You equip the {} in both hands.".format(params.lower()))
					
				elif (gameitems[params.lower()]["hands"] == 1) and ((players[id].weapon1 == None) or (players[id].weapon2 == None)):
					if players[id].weapon1 == None:
						players[id].weapon1 = params.lower()
						players[id].inventory.remove(params.lower())
						mud.send_message(id, "You equip the {} in your right hand.".format(params.lower()))
						
					else:
						players[id].weapon2 = params.lower()
						players[id].inventory.remove(params.lower())
						mud.send_message(id, "You equip the {} in your left hand.".format(params.lower()))
						
				else:
					mud.send_message(id, "Your hands are already full.")								
			
			elif gameitems[params.lower()]["type"] == "armor":
				if (gameitems[params.lower()]["slot"] == "chest") and (players[id].chest == None):
					players[id].chest = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} on your chest.".format(params.lower()))
					
				elif (gameitems[params.lower()]["slot"] == "helmet") and (players[id].helmet == None):
					players[id].helmet = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} on your head.".format(params.lower()))
			
				elif (gameitems[params.lower()]["slot"] == "legs") and (players[id].legs == None):
					players[id].legs = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} on your legs.".format(params.lower()))
					
				elif (gameitems[params.lower()]["slot"] == "gloves") and (players[id].gloves == None):
					players[id].gloves = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} on your hands.".format(params.lower()))
					
				elif (gameitems[params.lower()]["slot"] == "boots") and (players[id].boots == None):
					players[id].boots = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} on your feet.".format(params.lower()))
					
				elif (gameitems[params.lower()]["slot"] == "cloak") and (players[id].cloak == None):
					players[id].cloak = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} on your back.".format(params.lower()))
					
				elif (gameitems[params.lower()]["slot"] == "necklace") and (players[id].necklace == None):
					players[id].necklace = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} around your neck.".format(params.lower()))
					
				elif (gameitems[params.lower()]["slot"] == "ring") and (players[id].ring == None):
					players[id].ring = params.lower()
					players[id].inventory.remove(params.lower())
					mud.send_message(id, "You wear the {} on your finger.".format(params.lower()))
					
				else:
					mud.send_message(id, "You're already wearing a {}.".format(gameitems[params.lower()]["slot"]))				
		
		else:
			mud.send_message(id, "You cannot equip that.")
	
	else:
		mud.send_message(id, "You do not have a \"{}\"".format(params.lower()))