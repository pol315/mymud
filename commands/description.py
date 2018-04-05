import re

def Description(id, params, players, cursor, conn, mud):
	if params:
		description = re.sub('[^A-Za-z0-9\'.!?, ]+', '', params)
		
		if ((description[-1] is '.') or (description[-1] is '?') or (description[-1] is '!')):
			pass
		else:
			description = description + "."
			
		description = description.replace('\'', '\'\'')
		
		cursor.execute("""UPDATE player SET description = '{0}' WHERE username = '{1}';""".format(description, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()
			players[id].description = description
		
			mud.send_message(id, "Your description has been updated. Try LOOK ME or LOOK {} to review it.".format(players[id].name))	
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)
		
	else:
		mud.send_message(id, "Provide a description of your character.")