def Bank(id, players, rooms, mud):
	if rooms[players[id].room].roomtype == "bank":
		if players[id].bank:
			mud.send_message(id, "Your bank contains:\r\n{}".format("\r\n".join(players[id].bank)))
			
		else:
			mud.send_message(id, "There are no items in your bank currently.")

		mud.send_message(id, "Gold: {}".format(str(players[id].bankgold)), mud._BOLD, mud._YELLOW)
	
	else:
		mud.send_message(id, "You must be at a bank to check the contents of your account.")