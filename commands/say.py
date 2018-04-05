from classes.utilities import MakeProper

def Say(id, params, players, mud):
	for pid, pl in players.items():														# go through every player in the game		
		if players[pid].room == players[id].room: 								# if they're in the same room as the player
			mud.send_message(pid, "{} says \"{}\"".format(players[id].name, MakeProper(params))) # send them a message telling them what the player said