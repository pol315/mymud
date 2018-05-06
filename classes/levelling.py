from classes.utilities	import CalculateTotalStats

import math

LEVELLING_FUNCTION = 2.1

def GainLevel(id, players, gameitems, skill, cursor, conn, mud):
	if skill == "strength":
		players[id].strength += 1 
		mud.send_message(id, "Congratulations, you've reached strength level {}!".format(str(players[id].strength)))

		cursor.execute("UPDATE player SET strength_level = %s WHERE username = %s;", (players[id].strength, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)

	if skill == "dexterity":
		players[id].dexterity += 1 
		mud.send_message(id, "Congratulations, you've reached dexterity level {}!".format(str(players[id].dexterity)))

		cursor.execute("UPDATE player SET dexterity_level = %s WHERE username = %s;", (players[id].dexterity, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)

	if skill == "wisdom":
		players[id].wisdom += 1 
		mud.send_message(id, "Congratulations, you've reached wisdom level {}!".format(str(players[id].wisdom)))

		cursor.execute("UPDATE player SET wisdom_level = %s WHERE username = %s;", (players[id].wisdom, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

		CalculateTotalStats(id, players, gameitems, cursor, conn, mud)

	if skill == "endurance":
		players[id].endurance += 1 
		mud.send_message(id, "Congratulations, you've reached endurance level {}!".format(str(players[id].endurance)))

		cursor.execute("UPDATE player SET endurance_level = %s WHERE username = %s;", (players[id].endurance, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

	if skill == "clarity":
		players[id].clarity += 1 
		mud.send_message(id, "Congratulations, you've reached clarity level {}!".format(str(players[id].clarity)))

		cursor.execute("UPDATE player SET clarity_level = %s WHERE username = %s;", (players[id].clarity, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)
	

def GainExperience(id, players, gameitems, skill, xp, cursor, conn, mud):
	currXP = None
	currLevel = None

	if skill == "strength":
		players[id].strengthxp += xp
		currXP = players[id].strengthxp
		currLevel = players[id].strength

		cursor.execute("UPDATE player SET strength_xp = %s WHERE username = %s;", (players[id].strengthxp, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

	elif skill == "dexterity":
		players[id].dexterityxp += xp
		currXP = players[id].dexterityxp
		currLevel = players[id].dexterity

		cursor.execute("UPDATE player SET dexterity_xp = %s WHERE username = %s;", (players[id].dexterityxp, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

	elif skill == "wisdom":
		players[id].wisdomxp += xp
		currXP = players[id].wisdomxp
		currLevel = players[id].wisdom

		cursor.execute("UPDATE player SET wisdom_xp = %s WHERE username = %s;", (players[id].wisdomxp, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

	elif skill == "endurance":
		players[id].endurancexp += xp
		currXP = players[id].endurancexp
		currLevel = players[id].endurance

		cursor.execute("UPDATE player SET endurance_xp = %s WHERE username = %s;", (players[id].endurancexp, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

	elif skill == "clarity":
		players[id].clarityxp += xp
		currXP = players[id].clarityxp
		currLevel = players[id].clarity

		cursor.execute("UPDATE player SET clarity_xp = %s WHERE username = %s;", (players[id].clarityxp, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)

	
	if (currXP) and (currLevel) and (currXP >= (math.ceil((currLevel + 1)**LEVELLING_FUNCTION) * 100)):
		GainLevel(id, players, gameitems, skill, cursor, conn, mud)
		



		
	



