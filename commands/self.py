def Self(id, params, players, mud):
	mud.send_message(id, "================================================", mud._BOLD, mud._BLUE)
	mud.send_message(id, "|| Name:	{}              			        ||".format(players[id].name), mud._BOLD, mud._BLUE)
	mud.send_message(id, "|| Race:	{}				Gender:	{}			||".format(players[id].race.capitalize(), players[id].gender.capitalize()), mud._BOLD, mud._BLUE)
	mud.send_message(id, "|| Description: {} {}                         ||".format(players[id].name, players[id].description), mud._BOLD, mud._BLUE)
	mud.send_message(id, "||--------------------------------------------||", mud._BOLD, mud._BLUE)
	