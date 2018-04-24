# FIGHT is a basic skill known by all players
# the player makes a basic attack with the currently equipped weapon, or fists if no weapon equipped

import random

def Fight(id, params, players, rooms, gameitems, ticks, mud):

	if params.lower() in rooms[players[id].room].monsters:		# check if monster is here
		if players[id].balance:
			players[id].balance = False
			players[id].fight_tick = ticks

			attackpower = 0
			attack = "melee"		# using fists by default with a melee attack
			awith = "fists"

			if players[id].weapon1:	# weapon 1 is the main weapon, this decides the kind of attack we are making (melee, range, magic)

				awith = players[id].weapon1

				if gameitems[players[id].weapon1].attack == "melee":
					attackpower = attackpower + players[id].strength
					attackpower = attackpower + gameitems[players[id].weapon1].strength

				elif gameitems[players[id].weapon1].attack == "range":
					attackpower = attackpower + players[id].dexterity
					attackpower = attackpower + gameitems[players[id].weapon1].dexterity
					attack = "range"

				elif gameitems[players[id].weapon1].attack == "magic":
					attackpower = attackpower + players[id].wisdom
					attackpower = attackpower + gameitems[players[id].weapon1].wisdom
					attack = "magic"

			if players[id].weapon2:	# weapon 2 gets its stats added to the attack, but only the relevant stat to the first weapon (ie. a main hand sword and offhand staff, the staff would only contribute if it had a strength stat)

				if gameitems[players[id].weapon1].attack == "melee":
					attackpower = attackpower + gameitems[players[id].weapon2].strength

				elif gameitems[players[id].weapon1].attack == "range":
					attackpower = attackpower + gameitems[players[id].weapon2].dexterity

				elif gameitems[players[id].weapon1].attack == "magic":
					attackpower = attackpower + gameitems[players[id].weapon2].wisdom

		else:
			mud.send_message(id, "You need to regain your balance first!")

	else:
		mud.send_message(id, "You don't see that monster here.")

			
		

