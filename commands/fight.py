# FIGHT is a basic skill known by all players
# the player makes a basic attack with the currently equipped weapon, or fists if no weapon equipped

import random

from classes.combat		import DamageMonster
from classes.utilities	import AdvertiseToRoom

def Fight(id, params, players, rooms, gameitems, beastiary, monsterInstances, ticks, mud):

	monsterToFight = None

	if params:
		monsterToFight = params.lower()

	elif players[id].combat_target:
		monsterToFight = monsterInstances[players[id].combat_target].name

	if monsterToFight:

		monsterHere = False
		monsterID = -1

		for monster in monsterInstances:
			if (monsterInstances[monster].room == players[id].room) and (monsterToFight == monsterInstances[monster].name):
				monsterHere = True
				monsterID = monster
				break

		if monsterHere:
			if players[id].balance:
				players[id].balance = False
				players[id].fight_tick = ticks

				if (players[id].name in monsterInstances[monsterID].combat_target) is False:
					monsterInstances[monsterID].combat_target.append(players[id].name)

				attackpower = 0
				awith = "fists"
				mdefence = 0
				combattext = ["you punch as hard as you can.", "you let loose a flurry of kicks and punches.", "you uppercut your enemy with all your force."]

				if players[id].weapon1:	# weapon 1 is the main weapon, this decides the kind of attack we are making (melee, range, magic)
										# weapon 2 gets its stats added to the attack, but only the relevant stat to the first weapon (ie. a main hand sword and offhand staff, the staff would only contribute if it had a strength stat)
					awith = players[id].weapon1

					if gameitems[players[id].weapon1].attack == "melee":
						attackpower = players[id].totalstr
						mdefence = beastiary[monsterToFight].meleed
						combattext = ["you lash out with your weapon with great might.", "you let loose a flurry of stabs and jabs.", "you bring down your weapon as hard as you can."]

					elif gameitems[players[id].weapon1].attack == "range":
						attackpower = players[id].totaldex
						mdefence = beastiary[monsterToFight].ranged
						combattext = ["you pull back on the string as hard as you can and send an arrow flying.", "you let loose an arrow with great precision.", "you grab an arrow from your quiver and deliver it with speed."]

					elif gameitems[players[id].weapon1].attack == "magic":
						attackpower = players[id].totalwis
						mdefence = beastiary[monsterToFight].magicd
						combattext = ["you send a group of bolts hurtling at your opponent.", "you channel as much energy as you can into your enemy.", "you let loose a great ball of energy."]

				else:		# only attacking with fists
					attackpower = players[id].totalstr

				damage = random.randint(attackpower, (attackpower * 2))		# think of rolling x number of d2s
				damage = damage - mdefence

				AdvertiseToRoom(id, "{} attacks the {} with their {}, doing {} damage.".format(players[id].name, monsterToFight, awith, str(damage)), "With your {}, {}".format(awith, random.sample(combattext, 1)[0]), players, mud)				
				mud.send_message(id, "You deal {} damage.".format(str(damage)), mud._BOLD, mud._BLUE)

				DamageMonster(players, id, damage, monsterInstances, monsterID, beastiary, mud)			

			else:
				mud.send_message(id, "You need to regain your balance first!")

		else:
			mud.send_message(id, "You don't see that monster here.")

	else:
		mud.send_message(id, "You must specify a monster as a parameter or set a combat target using SETTARGET first.")

			
		

