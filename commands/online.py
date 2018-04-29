def Online(id, players, mud):
	online = list()
	
	for pl in players:
		online.append(players[pl].name)

	mud.send_message(id, "Players online:\r\n{}".format("\r\n".join(online)))
