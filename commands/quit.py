import datetime
import time
import math

def Quit(id, players, cursor, conn, ticks, mud):

	secondsplayed = math.floor((ticks - players[id].auth_tick) / 5)

	totalsecondsplayed = secondsplayed + players[id].playtime
	
	cursor.execute("UPDATE player SET play_time = %s WHERE username = %s;", (totalsecondsplayed, players[id].name))
	if cursor.rowcount == 1:
		conn.commit()	
	else:
		mud.send_message(id, "Could not update playtime.")
	
	mud.send_message(id, "You sit on the ground and slowly fade from view...")
	mud.send_message(id, "Come back soon, {}.".format(players[id].name))
	mud.terminate_connection(id) # TODO: handle saving client state to the database before quitting