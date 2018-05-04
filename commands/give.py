from classes.utilities	import AdvertiseToRoom
from classes.utilities	import TeleportPlayer
from classes.utilities	import ParseAlias

def Give(id, params, players, rooms, gameitems, npcs, beastiary, monsterInstances, cursor, conn, mud):

	if (params) and (" to " in params):
		item = params.lower().split(" to ")[0]
		target = params.lower().split(" to ")[1]

		itemalias = ParseAlias(id, item, players, rooms, None, "inventory")
		targetalias = ParseAlias(id, target, players, rooms, None, "npcs")


		if (itemalias) and (itemalias in players[id].inventory):
			if (targetalias) and (rooms[players[id].room].npcs) and (targetalias in rooms[players[id].room].npcs):
				
				given = False

				if (itemalias == "beginners ticket") and (targetalias == "glorifa"):
					gstring = "Glorifa says \"Congratulations {}, with the passing of this ticket you've graduated from the Beginner's Academy and will now be transported to the world of MyMud. Remember to ask your fellow adventurer or use the HELP command if you become lost.\"".format(players[id].name)
					AdvertiseToRoom(id, gstring, gstring, players, mud)
					TeleportPlayer(id, "Antiqua - Main Plaza", players, rooms, gameitems, npcs, beastiary, monsterInstances, mud)
					given = True

				else:
					mud.send_message(id, "That person doesn't want that item.")		

				if given:
					players[id].inventory.remove(itemalias)

					cursor.execute("UPDATE player SET inventory = %s WHERE username = %s;", (players[id].inventory, players[id].name))
					if cursor.rowcount == 1:
						conn.commit()	
					else:
						mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
						mud.terminate_connection(id)

			else:
				mud.send_message(id, "That person isn't here.")	
		
		else:
			mud.send_message(id, "You don't have that item.")

	else:
		mud.send_message(id, "Give what to whom?")

