import random


BALANCE_TICKS = 20

def MonsterBasicAttack(monsterID, playerID, players, monsterInstances, ticks, mud):
	monsterInstances[monsterID].balance = False
	monsterInstances[monsterID].fight_tick = ticks

	attackpower = 0
	pdefence = 0

	if monsterInstances[monsterID].attack == "melee":
		attackpower = attackpower + monsterInstances[monsterID].strength
		pdefence = players[playerID].meleed

	elif monsterInstances[monsterID].attack == "range":
		attackpower = attackpower + monsterInstances[monsterID].dexterity
		pdefence = players[playerID].ranged

	elif monsterInstances[monsterID].attack == "magic":
		attackpower = attackpower + monsterInstances[monsterID].wisdom
		pdefence = players[playerID].magicd

	damage = random.randint(attackpower, (attackpower * 2))		# think of rolling x number of d2s
	damage = damage - pdefence

	players[playerID].hp -= damage

	mud.send_message(playerID, "{} attacks you and deals {} damage.".format(monsterInstances[monsterID].name.title(), str(damage)), mud._BOLD, mud._RED)


def RegainBalance(players, monsterInstances, ticks, mud):	# regain players and monsters balances
	for pl in players:
		if (players[pl].balance is False) and (ticks >= (players[pl].fight_tick + BALANCE_TICKS)):
			players[pl].balance = True
			mud.send_message(pl, "You regain your balance.", mud._BOLD, mud._CYAN)
			mud.send_message(pl, "")

	for monster in monsterInstances:
		if (monsterInstances[monster].balance is False) and (ticks >= (monsterInstances[monster].fight_tick + monsterInstances[monster].attack_speed)):
			monsterInstances[monster].balance = True	


def MonsterAttacks(players, monsterInstances, ticks, mud): # if a monster has a combat target and balance, and the target is in the same room, attack
	for monster in monsterInstances:
		if monsterInstances[monster].combat_target and monsterInstances[monster].balance:
			target = monsterInstances[monster].combat_target

			for pl in players:
				if (players[pl].name == target) and (players[pl].room == monsterInstances[monster].room):
					MonsterBasicAttack(monster, pl, players, monsterInstances, ticks, mud)


def ForgetTargets(monsterInstances, ticks):	# monsters forget their target after 30 seconds of no fighting action
	for monster in monsterInstances:
		if (monsterInstances[monster].combat_target) and (ticks >= (monsterInstances[monster].fight_tick + 150)):
			monsterInstances[monster].combat_target = None
