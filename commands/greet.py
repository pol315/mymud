from classes.utilities import AdvertiseToRoom

def Greet(id, params, players, rooms, npcs, mud):
	if params:          # greet someone specific
		if ("npcs" in rooms[players[id].room]) and (params.lower() in rooms[players[id].room]["npcs"]):
			AdvertiseToRoom(id, "{} greets {} with a wave and a smile.".format(players[id].name, params.lower().title()), "You greet {} with a wave and a smile.".format(params.lower().title()), players, mud)
			
			if "response" in npcs[params.lower()]:
				AdvertiseToRoom(id, "{} responds, \"{}\"".format(params.lower().title(), npcs[params.lower()]["response"]), "{} responds, \"{}\"".format(params.lower().title(), npcs[params.lower()]["response"]), players, mud)

		else:
			greeted = False
			
			for pid, pl in players.items():
				if players[pid].room == players[id].room:
					if players[pid].name.lower() == params.lower():
						AdvertiseToRoom(id, "{} greets {} with a wave and a smile.".format(players[id].name, params.lower().capitalize()), "You greet {} with a wave and a smile.".format(params.lower().capitalize()), players, mud)                                                
						greeted = True

			if greeted == False:
				mud.send_message(id, "You do not see that person here.") 
	
	else:                   # greet everyone in room
		AdvertiseToRoom(id, "{} greets everyone in the area with a wave and a smile.".format(players[id].name), "You greet everyone in the area with a wave and a smile.", players, mud)

