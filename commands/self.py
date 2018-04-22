def Self(id, params, players, mud):
    mud.send_message(id, "================================================", mud._BOLD, mud._BLUE)
    mud.send_message(id, "|| Name:	{}              			        ||".format(players[id].Name), mud._BOLD, mud._BLUE)
	mud.send_message(id, "|| Race:	{}				Gender:	{}			||".format(players[id].Race, players[id].Gender), mud._BOLD, mud._BLUE)
    mud.send_message(id, "|| Description: {}                            ||".format(players[id].Description), mud._BOLD, mud._BLUE)
	