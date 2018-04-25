import re
import time

from random import randint
from pbkdf2 import crypt
from classes.utilities import PlacePlayerInGame

def HashPass(passw,salt):
	return str(crypt(passw,salt,iterations=5000))
	
def IsValidPass(passw,salt,dbHash):
	result = crypt(passw,salt,iterations=5000)
	return str(result) == dbHash
	
def ValidateName(id, command, players, cursor, mud):
	if re.match(r'^[A-Za-z]{3,12}$', command):				
		players[id].name = command.capitalize()
		
		# search db for username - if not exist create new user, if exist prompt for password
		cursor.execute("SELECT * FROM player WHERE username = %s;", (players[id].name,))
		rows = cursor.fetchall()
		
		if len(rows) == 1:
			players[id].exist = True
			mud.send_message(id, "Welcome back {}!".format(players[id].name))
			mud.send_message(id, "Please enter your password:", nr=False)										
			
		else:
			mud.send_message(id, "You seem to be new here, {}, welcome!".format(players[id].name))
			mud.send_message(id, "Let's start by entering a password you'll use to log in:", nr=False)
			
		mud.obscure_input(id)			
	
	else:
		mud.send_message(id, "Username must start with a capital letter, consist of only letters and must be between 3 and 12 characters. Try again!")
		
def LogPlayerIn(id, command, players, rooms, gameitems, npcs, monsters, cursor, conn, mud):

	players[id].last_command = ""

	cursor.execute("SELECT password, salt, last_login, last_room, description, gender, race, inventory, chest, helmet, legs, boots, gloves, cloak, necklace, ring, weapon1, weapon2, totalstr, totaldex, totalwis, meleed, ranged, magicd FROM player WHERE username = %s;", (players[id].name,))
	rows = cursor.fetchall()						
	
	if IsValidPass(command,str(rows[0][1]),str(rows[0][0])):
		if any(((pl.name == players[id].name) and (pl.gender)) for pl in players.values()):
			mud.send_message(id, "\r\nYou are already logged into the game!")								
			mud.terminate_connection(id)
		
		else:
			players[id].last_login = rows[0][2]
			players[id].room = rows[0][3]
			
			if rows[0][4] is not None:
				players[id].description = rows[0][4]					
			
			players[id].gender = rows[0][5]
			players[id].race = rows[0][6]
			
			if rows[0][7] is not None:
				players[id].inventory = rows[0][7]
				
			players[id].chest = rows[0][8]
			players[id].helmet = rows[0][9]
			players[id].legs = rows[0][10]
			players[id].boots = rows[0][11]
			players[id].gloves = rows[0][12]
			players[id].cloak = rows[0][13]
			players[id].necklace = rows[0][14]
			players[id].ring = rows[0][15]
			players[id].weapon1 = rows[0][16]
			players[id].weapon2 = rows[0][17]

			players[id].totalstr = int(rows[0][18])
			players[id].totaldex = int(rows[0][19])
			players[id].totalwis = int(rows[0][20])
			players[id].meleed = int(rows[0][21])
			players[id].ranged = int(rows[0][22])
			players[id].magicd = int(rows[0][23])
			
			
			mud.send_message(id, "\r\n\r\nYou last logged in at: {}".format(players[id].last_login))
		
			players[id].authenticated = True
			mud.show_input(id)
			
			timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
			
			cursor.execute("UPDATE player SET last_login = %s WHERE username = %s;", (timestamp, players[id].name))
			if cursor.rowcount == 1:
				conn.commit()	
			else:
				mud.send_message(id, "Could not update timestamp.")
				mud.terminate_connection(id)
			
			PlacePlayerInGame(id, players, rooms, gameitems, npcs, monsters, mud)
		
	else:
		mud.send_message(id, "\r\nIncorrect password.")								
		mud.terminate_connection(id)
		
def CreateNewUser(id, command, players, cursor, conn, mud):
	if command == players[id].pw1:
		salt = str(randint(1000000,9999999)				)
		passw = HashPass(command, salt)
		timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
		
		cursor.execute("INSERT INTO player (username, password, created_on, last_login, salt, last_room) VALUES (%s, %s, %s, %s, %s, %s) RETURNING user_id", (players[id].name, passw, timestamp, timestamp, salt, "Hall of Beginnings"))
		dbid = cursor.fetchone()[0]
		if dbid:
			conn.commit()
			
			players[id].authenticated = True
			players[id].exist = True
			players[id].pw1 = ""
			players[id].last_login = timestamp
			mud.show_input(id)
			
			mud.send_message(id, "\r\nWill your character be male or female?")
		else:
			mud.send_message(id, "\r\nDidn't work my dude. See ya later.")
			mud.terminate_connection(id)
		
	else: 
		mud.send_message(id, "\r\nPasswords don't match.")
		mud.terminate_connection(id)