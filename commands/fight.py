# FIGHT is a basic skill known by all players
# the player makes a basic attack with the currently equipped weapon, or fists if no weapon equipped

import random

def Fight(id, params, players, rooms, gameitems, monsters, ticks, mud):

	if params.lower() in rooms[players[id].room].monsters:		# check if monster is here
		if players[id].balance:
			players[id].balance = False
			players[id].fight_tick = ticks

			rooms[players[id].room].monsters[params.lower()].combat_target = players[id].name
			rooms[players[id].room].monsters[params.lower()].fight_tick = ticks

			attackpower = 0
			awith = "fists"
			mdefence = 0
			combattext = ["you punch as hard as you can.", "you let loose a flurry of kicks and punches.", "you uppercut your enemy with all your force."]

			if players[id].weapon1:	# weapon 1 is the main weapon, this decides the kind of attack we are making (melee, range, magic)
									# weapon 2 gets its stats added to the attack, but only the relevant stat to the first weapon (ie. a main hand sword and offhand staff, the staff would only contribute if it had a strength stat)
				awith = players[id].weapon1

				if gameitems[players[id].weapon1].attack == "melee":
					attackpower = players[id].totalstr
					mdefence = monsters[params.lower()].meleed
					combattext = ["you lash out with your weapon with great might.", "you let loose a flurry of stabs and jabs.", "you bring down your weapon as hard as you can."]

				elif gameitems[players[id].weapon1].attack == "range":
					attackpower = players[id].totaldex
					mdefence = monsters[params.lower()].ranged
					combattext = ["you pull back on the string as hard as you can and send an arrow flying.", "you let loose an arrow with great precision.", "you grab an arrow from your quiver and deliver it with speed."]

				elif gameitems[players[id].weapon1].attack == "magic":
					attackpower = players[id].totalwis
					mdefence = monsters[params.lower()].magicd
					combattext = ["you send a group of bolts hurtling at your opponent.", "you channel as much energy as you can into your enemy.", "you let loose a great ball of energy."]

			else:		# only attacking with fists
				attackpower = players[id].totalstr

			damage = random.randint(attackpower, (attackpower * 2))		# think of rolling x number of d2s
			damage = damage - mdefence

			mud.send_message(id, "With your {}, {}".format(awith, random.sample(combattext, 1)[0]), mud._BOLD, mud._YELLOW)
			mud.send_message(id, "You deal {} damage.".format(str(damage)), mud._BOLD, mud._BLUE)

			rooms[players[id].room].monsters[params.lower()].hp -= damage

			if rooms[players[id].room].monsters[params.lower()].hp <= 0:
				mud.send_message(id, "You kill the {}.".format(params.lower()))
				del rooms[players[id].room].monsters[params.lower()]

				#TODO push attack power calculation into separate method
				#TODO push monster hp calculation into separate method
				#TODO monster drops

		else:
			mud.send_message(id, "You need to regain your balance first!")

	else:
		mud.send_message(id, "You don't see that monster here.")

			
		

