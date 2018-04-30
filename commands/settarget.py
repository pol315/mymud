def SetTarget(id, params, players, beastiary, monsterInstances, mud):
	if params:
		if params.lower() in beastiary:
			targetted = False

			for monster in monsterInstances:
				if (monsterInstances[monster].room == players[id].room) and (monsterInstances[monster].name == params.lower()):
					players[id].combat_target = monster
					targetted = True
					break

			if targetted:
				mud.send_message(id, "You set your current combat target to \"{}\".".format(params.lower()))
			else:
				mud.send_message(id, "You don't see that monster here.")

		else:
			mud.send_message(id, "That monster does not exist.")	
	
	else:
		mud.send_message(id, "You must specify the target.")