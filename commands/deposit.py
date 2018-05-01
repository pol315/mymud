def Deposit(id, params, players, rooms, cursor, conn, mud):
	if rooms[players[id].room].roomtype == "bank":
		if params:
			if '-' in params:
				mud.send_message(id, "You can't deposit negative gold.")	

			else:
				if params.isdigit():			# depositing gold
					goldToDeposit = int(params)

					if goldToDeposit <= players[id].gold:
						players[id].bankgold += goldToDeposit
						players[id].gold -= goldToDeposit

						cursor.execute("UPDATE player SET gold = %s, bankgold = %s WHERE username = %s;", (players[id].gold, players[id].bankgold, players[id].name))
						if cursor.rowcount == 1:
							conn.commit()	
						else:
							mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
							mud.terminate_connection(id)

						mud.send_message(id, "You deposit {} gold into the bank.".format(params))

					else:
						mud.send_message(id, "You don't have that much gold.")

				
				else:							# depositing item
					if params.lower() in players[id].inventory:
						if len(players[id].bank) <= 100:
							players[id].inventory.remove(params.lower())
							players[id].bank.append(params.lower())

							cursor.execute("UPDATE player SET inventory = %s, bank = %s WHERE username = %s;", (players[id].inventory, players[id].bank, players[id].name))
							if cursor.rowcount == 1:
								conn.commit()	
							else:
								mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
								mud.terminate_connection(id)

							mud.send_message(id, "You deposit \"{}\" into the bank.".format(params.lower()))

						else:
							mud.send_message(id, "Your bank is full.")				
					
					else:
						mud.send_message(id, "You aren't carrying \"{}\".".format(params.lower()))			
		
		else:
			mud.send_message(id, "Deposit what?")

	else:
		mud.send_message(id, "You need to be at a bank to deposit items or gold.")