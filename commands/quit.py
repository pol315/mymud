from datetime import datetime
import time

def Quit(id, players, cursor, conn, mud):

	d1 = datetime.strptime(str(players[id].last_login), "%Y-%m-%d %H:%M:%S")
	d2 = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
	preplaytime = players[id].playtime
	sessiontime = d2 - d1
	totaltime = preplaytime + sessiontime
	
	cursor.execute("UPDATE player SET play_time = %s WHERE username = %s;", (totaltime, players[id].name))
	if cursor.rowcount == 1:
		conn.commit()	
	else:
		mud.send_message(id, "Could not update playtime.")
	
	mud.send_message(id, "You sit on the ground and slowly fade from view...")
	mud.send_message(id, "Come back soon, {}.".format(players[id].name))
	mud.terminate_connection(id) # TODO: handle saving client state to the database before quitting