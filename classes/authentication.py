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
		cursor.execute("""SELECT * FROM player WHERE username = '{}'""".format(players[id].name))
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
		
def LogPlayerIn(id, command, players, rooms, cursor, conn, mud):
	cursor.execute("""SELECT password, salt, last_login, last_room, description, gender, race FROM player WHERE username = '{}'""".format(players[id].name))
	rows = cursor.fetchall()						
	
	if IsValidPass(command,str(rows[0][1]),str(rows[0][0])):
	
		players[id].last_login = rows[0][2]
		players[id].room = rows[0][3]
		
		if rows[0][4] is not None:
			players[id].description = rows[0][4]					
		
		players[id].gender = rows[0][5]
		players[id].race = rows[0][6]
		
		
		mud.send_message(id, "\r\n\r\nYou last logged in at: {}".format(players[id].last_login))
		#TODO user already authenticated?
	
		players[id].authenticated = True
		mud.show_input(id)
		
		timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
		
		cursor.execute("""UPDATE player SET last_login = '{0}' WHERE username = '{1}';""".format(timestamp, players[id].name))
		if cursor.rowcount == 1:
			conn.commit()	
		else:
			mud.send_message(id, "Could not update timestamp.")
			mud.terminate_connection(id)
		
		PlacePlayerInGame(id, players, rooms, mud)
		
	else:
		mud.send_message(id, "\r\nIncorrect password.")								
		mud.terminate_connection(id)
		
def CreateNewUser(id, command, players, rooms, cursor, conn, mud):
	if command == players[id].pw1:
		salt = str(randint(1000000,9999999)				)
		passw = HashPass(command, salt)
		timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
		
		cursor.execute("""INSERT INTO player (username, password, created_on, last_login, salt, last_room) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}') RETURNING user_id""".format(players[id].name, passw, timestamp, timestamp, salt, "Hall of Beginnings"))
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