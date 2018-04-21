from commands.look		import Look

def MakeProper(message):		
	if ((message[-1] is '.') or (message[-1] is '?') or (message[-1] is '!')):
		pass
	else:
		message = message + "."
		
	return message.capitalize()
	
def PlacePlayerInGame(id, players, rooms, gameitems, npcs, monsters, mud):

	if ((players[id].room is None) or (players[id].room is "")):
		players[id].room = "Hall of Beginnings"

	for pid, pl in players.items():																									# go through all the players in the game
		if pid != id:
			mud.send_message(pid, "{} has entered the game".format(players[id].name))												# send each player a message to tell them about the new player

	mud.send_message(id, "\r\nWelcome to the game, {}. ".format(players[id].name) + "Type 'help' if you get lost. Have fun!")		# send the new player a welcome message			
	mud.send_message(id, "")		
	Look(id, None, players, rooms, gameitems, npcs, monsters, mud)														# send the new player the description of their current room

def AdvertiseToRoom(id, message, selfmessage, players, mud):
	if selfmessage is not None:
		mud.send_message(id, selfmessage)

	for pid, pl in players.items():														
		if (pid != id) and (players[pid].room == players[id].room):
			mud.send_message(pid, message)