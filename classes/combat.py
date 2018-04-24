
BALANCE_TICKS = 20


def RegainBalance(players, ticks, mud):
	for pl in players:
		if (players[pl].balance is False) and (ticks >= (players[pl].fight_tick + BALANCE_TICKS)):
			players[pl].balance = True
			mud.send_message(pl, "You regain your balance.", mud._BOLD, mud._CYAN)
			
