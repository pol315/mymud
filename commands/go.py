from commands.look	import Look

def Go(id, params, rooms, gameitems, npcs, beastiary, monsterInstances, players, cursor, conn, mud):
	ex = params.lower()																				# store the exit name
	rm = rooms[players[id].room]																	# store the player's current room
				
	if ex in rm.exits:																			# if the specified exit is found in the room's exits list
		for pid, pl in players.items():																# go through all the players in the game
			if players[pid].room == players[id].room and pid != id:							# if player is in the same room and isn't the player sending the command
				mud.send_message(pid, "{} left, going {}".format(players[id].name, ex))			# send them a message telling them that the player left the room
					
		players[id].room = rm.exits[ex]														# update the player's current room to the one the exit leads to
		rm = rooms[players[id].room]
		
		cursor.execute("UPDATE player SET last_room = %s WHERE username = %s;", (players[id].room, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)
		
		for pid, pl in players.items():																# go through all the players in the game
			if players[pid].room == players[id].room and pid != id:							# if player is in the same (new) room and isn't the player sending the command						
				if ex is "down":
					mud.send_message(pid, "{} arrived from above".format(players[id].name))
				elif ex is "up":
					mud.send_message(pid, "{} arrived from below".format(players[id].name))
				else:				
					mud.send_message(pid, "{} arrived from the {}".format(players[id].name, ex))	    # send them a message telling them that the player entered the room

		# send the player a message telling them where they are now
		Look(id, None, players, rooms, gameitems, npcs, beastiary, monsterInstances, mud)

				
	else:																							# the specified exit wasn't found in the current room
		mud.send_message(id, "That is not a way you can go.")										# send back an 'unknown exit' message