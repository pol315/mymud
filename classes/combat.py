import random
from classes.utilities	import AdvertiseToRoom

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
	
	if damage < 0:	# don't want monsters healing players...
		damage = 0

	players[playerID].hp -= damage

	AdvertiseToRoom(playerID, "{} attacks {} and deals {} damage.".format(monsterInstances[monsterID].name.title(), players[playerID].name, str(damage)), "{} attacks you and deals {} damage.".format(monsterInstances[monsterID].name.title(), str(damage)), players, mud, mud._BOLD, mud._RED)


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
			target = None
			attacked = False
			for tg in monsterInstances[monster].combat_target:
				
				for pl in players:
					if (players[pl].name == tg) and (players[pl].room == monsterInstances[monster].room):
						target = monsterInstances[monster].combat_target
						attacked = True
						MonsterBasicAttack(monster, pl, players, monsterInstances, ticks, mud)
						break

				if attacked:
					break


def ForgetTargets(monsterInstances, ticks):	# monsters forget their target after 30 seconds of no fighting action	# TODO should monsters "leash" (refill their health when no one has attacked them in a while)
	for monster in monsterInstances:
		if (monsterInstances[monster].combat_target) and (ticks >= (monsterInstances[monster].fight_tick + 150)):
			monsterInstances[monster].combat_target = list()


def DamageMonster(players, playerID, damage, monsterInstances, monsterID, beastiary, mud):
	monsterInstances[monsterID].hp -= damage

	if monsterInstances[monsterID].hp <= 0:
		
		AdvertiseToRoom(playerID, "{} kills the {}.".format(players[playerID].name, monsterInstances[monsterID].name.title()), "You kill the {}.".format(monsterInstances[monsterID].name.title()), players, mud, mud._BOLD, mud._GREEN)

		# drops
		itemDrops = list()

		for key in beastiary[monsterInstances[monsterID].name].drops:
			if ((random.random() + 0.001) * 100 ) < int(beastiary[monsterInstances[monsterID].name].drops[key]):
				players[playerID].inventory.append(key)
				itemDrops.append(key)

		if itemDrops:
			mud.send_message(playerID, "You pick up the following items from your dead opponent: {}".format(", ".join(itemDrops)), mud._BOLD, mud._GREEN)

		del monsterInstances[monsterID]


