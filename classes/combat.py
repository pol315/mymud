import random


BALANCE_TICKS = 20

def MonsterBasicAttack(currRoom, currMonster, playerID, players, rooms, ticks, mud):
	rooms[currRoom].monsters[currMonster].balance = False
	rooms[currRoom].monsters[currMonster].fight_tick = ticks

	attackpower = 0
	pdefence = 0

	if rooms[currRoom].monsters[currMonster].attack == "melee":
		attackpower = attackpower + rooms[currRoom].monsters[currMonster].strength
		pdefence = players[playerID].meleed

	elif rooms[currRoom].monsters[currMonster].attack == "range":
		attackpower = attackpower + rooms[currRoom].monsters[currMonster].dexterity
		pdefence = players[playerID].ranged

	elif rooms[currRoom].monsters[currMonster].attack == "magic":
		attackpower = attackpower + rooms[currRoom].monsters[currMonster].wisdom
		pdefence = players[playerID].magicd

	damage = random.randint(attackpower, (attackpower * 2))		# think of rolling x number of d2s
	damage = damage - pdefence

	players[playerID].hp -= damage

	mud.send_message(playerID, "{} attacks you and deals {} damage.".format(currMonster.title(), str(damage)), mud._BOLD, mud._RED)


def RegainBalance(players, rooms, ticks, mud):	# regain players and monsters balances
	for pl in players:
		if (players[pl].balance is False) and (ticks >= (players[pl].fight_tick + BALANCE_TICKS)):
			players[pl].balance = True
			mud.send_message(pl, "You regain your balance.", mud._BOLD, mud._CYAN)
			mud.send_message(pl, "")

	for room in rooms:
		if rooms[room].monsters:
			for key in rooms[room].monsters:
				if (rooms[room].monsters[key].balance is False) and (ticks >= (rooms[room].monsters[key].fight_tick + rooms[room].monsters[key].attack_speed)):
					rooms[room].monsters[key].balance = True


def MonsterAttacks(players, rooms, ticks, mud): # if a monster has a combat target and balance, and the target is in the same room, attack
	for room in rooms:
		if rooms[room].monsters:
			for key in rooms[room].monsters:
				if rooms[room].monsters[key].combat_target and rooms[room].monsters[key].balance:
					target = rooms[room].monsters[key].combat_target

					for pl in players:
						if (players[pl].name == target) and (players[pl].room == room):
							MonsterBasicAttack(room, key, pl, players, rooms, ticks, mud)


def ForgetTargets(rooms, ticks):	# monsters forget their target after 30 seconds of no fighting action
	for room in rooms:
		if rooms[room].monsters:
			for key in rooms[room].monsters:
				if (rooms[room].monsters[key].combat_target) and (ticks >= (rooms[room].monsters[key].fight_tick + 150)):
					rooms[room].monsters[key].combat_target = None
							

			
