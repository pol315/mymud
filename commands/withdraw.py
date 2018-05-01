def Withdraw(id, params, players, rooms, cursor, conn, mud):
	if rooms[players[id].room].roomtype == "bank":
		if params:
			if '-' in params:
				mud.send_message(id, "You can't withdraw negative gold.")	

			else:
				if params.isdigit():			# withdrawing gold
					goldToWithdraw = int(params)

					if goldToWithdraw <= players[id].bankgold:
						players[id].gold += goldToWithdraw
						players[id].bankgold -= goldToWithdraw

						cursor.execute("UPDATE player SET gold = %s, bankgold = %s WHERE username = %s;", (players[id].gold, players[id].bankgold, players[id].name))
						if cursor.rowcount == 1:
							conn.commit()	
						else:
							mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
							mud.terminate_connection(id)

						mud.send_message(id, "You withdraw {} gold from the bank.".format(params))

					else:
						mud.send_message(id, "You don't have that much gold in the bank.")

				
				else:							# withdrawing item
					if params.lower() in players[id].bank:
						players[id].inventory.append(params.lower())
						players[id].bank.remove(params.lower())

						cursor.execute("UPDATE player SET inventory = %s, bank = %s WHERE username = %s;", (players[id].inventory, players[id].bank, players[id].name))
						if cursor.rowcount == 1:
							conn.commit()	
						else:
							mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
							mud.terminate_connection(id)

						mud.send_message(id, "You withdraw \"{}\" from the bank.".format(params.lower()))
					
					else:
						mud.send_message(id, "That item isn't in your bank.")			
		
		else:
			mud.send_message(id, "Withdraw what?")

	else:
		mud.send_message(id, "You need to be at a bank to withdraw items or gold.")