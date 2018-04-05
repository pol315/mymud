from classes.utilities import MakeProper

def Tell(id, params, players, mud):
	paramlist = params.split(" ")
	if len(paramlist) <= 1:
		mud.send_message(id, "Tell whom what?")
	else:	
		pname = paramlist[0].title()
		del paramlist[0]
		message = " ".join(paramlist)
		delivered = False
	
		for pid, pl in players.items():																				# go through every player in the game		
			if players[pid].name == pname: 																		# if they're the tell recipient
				mud.send_message(pid, "{} says \"{}\"".format(players[id].name, MakeProper(message)), mud._BOLD, mud._YELLOW) # send them the message
				mud.send_message(id, "You tell {}: \"{}\"".format(pname, MakeProper(message)), mud._BOLD, mud._YELLOW)
				delivered = True
				
		if delivered is False:
			mud.send_message(id, "No player by that name is online.")
				