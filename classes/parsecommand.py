from classes.authentication import CreateNewUser
from classes.utilities		import DisplayPrompt
from classes.authentication import LogPlayerIn
from classes.authentication import ValidateName
from classes.utilities		import PlacePlayerInGame

from classes.player   		import _Player
from classes.server 		import _Server

from commands.description	import Description
from commands.drop			import Drop
from commands.emote			import Emote
from commands.equip			import Equip
from commands.fight			import Fight
from commands.go 			import Go
from commands.greet			import Greet
from commands.help 			import Help
from commands.inventory		import Inventory
from commands.look 			import Look
from commands.playtime		import Playtime
from commands.say 			import Say
from commands.self 			import Self
from commands.skills		import Skills
from commands.take 			import Take
from commands.tell 			import Tell
from commands.unequip		import Unequip
from commands.quit 			import Quit

from configparser 	  		import SafeConfigParser

import psycopg2
import json
import time

def ParseCommand(id, command, params, players, rooms, gameitems, npcs, beastiary, monsterInstances, ticks, cursor, conn, mud):
	
	if (command != "") and (command != "r"):
		players[id].last_command = command
		players[id].last_params = params

	if players[id].name is None and command != "":	# if the player hasn't given their name yet, use this first command as their name and move them to the starting room.
		ValidateName(id, command, players, cursor, mud)

	elif players[id].name is not None and players[id].exist is True and players[id].authenticated is False:							# The player exists and we are waiting for a password
		LogPlayerIn(id, command, players, rooms, gameitems, npcs, beastiary, monsterInstances, cursor, conn, mud)

	elif players[id].name is not None and players[id].exist is False and players[id].authenticated is False and players[id].pw1 is None:		# The player doesn't exist and we are setting a new password
		players[id].pw1 = command
		mud.send_message(id, "\r\nPlease type your password again:", nr=False)

	elif players[id].name and players[id].exist is False and players[id].authenticated is False and players[id].pw1:	# The player has typed their password a second time
		CreateNewUser(id, command, players, cursor, conn, mud)

	elif players[id].name and players[id].exist and players[id].authenticated and players[id].gender is None:	# The player just created an account and needs to decide gender
		if (command == "male") or (command == "female"):
			cursor.execute("UPDATE player SET gender = %s WHERE username = %s;", (command, players[id].name))
			if cursor.rowcount == 1:
				conn.commit()
				players[id].gender = command
				mud.send_message(id, "And what race would you like to be?")
				mud.send_message(id, "Human - balanced combat stats")
				mud.send_message(id, "Marduk - lizard-like humanoids - strength based")
				mud.send_message(id, "Avine - winged humanoids - dexterity based")
				mud.send_message(id, "Enerkin - humanoids composed of pure energy - wisdom based")
				mud.send_message(id, "Geblit - shorty, stalky humanoids - starts with no combat stats, but increased trade skills")
			else:
				mud.send_message(id, "Could not update gender.")
				mud.terminate_connection(id)

		else:
			mud.send_message(id, "Input not recognized. Will your character be male or female?")

	elif players[id].name and players[id].exist and players[id].authenticated and players[id].gender and players[id].race is None:	# The player just created an account and needs to decide race
		if (command == "human") or (command == "marduk") or (command == "avine") or (command == "enerkin") or (command == "geblit"):
			cursor.execute("UPDATE player SET race = %s WHERE username = %s;", (command, players[id].name))
			if cursor.rowcount == 1:
				conn.commit()
				players[id].race = command
				PlacePlayerInGame(id, players, rooms, gameitems, npcs, beastiary, mud)
			else:
				mud.send_message(id, "Could not update race.")
				mud.terminate_connection(id)

		else:
			mud.send_message(id, "Input not recognized. What race will your character be?")

	elif command == "help":
		Help(id, params, mud)
		DisplayPrompt(id, players, mud)

	elif command == "say":
		Say(id, params, players, mud)
		DisplayPrompt(id, players, mud)

	elif command == "tell":
		Tell(id, params, players, mud)
		DisplayPrompt(id, players, mud)

	elif command == "emote":
		Emote(id, params, players, mud)
		DisplayPrompt(id, players, mud)

	elif command == "description":
		Description(id, params, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif (command == "look") or (command == "l"):
		Look(id, params, players, rooms, gameitems, npcs, beastiary, monsterInstances, mud)
		DisplayPrompt(id, players, mud)

	elif command == "greet":
		Greet(id, params, players, rooms, npcs, mud)
		DisplayPrompt(id, players, mud)

	elif command == "playtime":
		Playtime(id, players, mud)
		DisplayPrompt(id, players, mud)
		
	elif command == "skills":
		Skills(id, params, players, mud)
		DisplayPrompt(id, players, mud)
		
	elif command == "take":
		Take(id, params, players, rooms, gameitems, cursor, conn, mud)
		DisplayPrompt(id, players, mud)
		
	elif command == "drop":
		Drop(id, params, players, rooms, cursor, conn, mud)
		DisplayPrompt(id, players, mud)
		
	elif (command == "inventory") or (command == "inv"):
		Inventory(id, params, players, mud)
		DisplayPrompt(id, players, mud)
		
	elif (command == "equip") or (command == "wear"):
		Equip(id, params, players, gameitems, cursor, conn, mud)
		DisplayPrompt(id, players, mud)
		
	elif (command == "unequip") or (command == "remove"):
		Unequip(id, params, players, gameitems, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	# COMBAT
	elif command == "fight":
		Fight(id, params, players, rooms, gameitems, beastiary, monsterInstances, ticks, mud)
		DisplayPrompt(id, players, mud)

	# MOVEMENT
	elif command == "go":
		Go(id, params, rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif (command == "north") or (command == "south") or (command == "east") or (command == "west") or (command == "northwest") or (command == "northeast") or (command == "southwest") or (command == "southeast") or (command == "up") or (command == "down"):
		Go(id, command, rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "n":
		Go(id, "north", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "s":
		Go(id, "south", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "w":
		Go(id, "west", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "e":
		Go(id, "east", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "nw":
		Go(id, "northwest", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "ne":
		Go(id, "northeast", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "sw":
		Go(id, "southwest", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "se":
		Go(id, "southeast", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "u":
		Go(id, "up", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	elif command == "d":
		Go(id, "down", rooms, players, cursor, conn, mud)
		DisplayPrompt(id, players, mud)

	# ADMIN COMMANDS
	elif command == "ticks" and players[id].name == "Doomblade":
		mud.send_message(id, "{}".format(ticks))
		DisplayPrompt(id, players, mud)

	# MISC
	elif (command == "quit") or (command == "qq"):
		Quit(id, players, cursor, conn, mud)
		
	elif command == "r":
		ParseCommand(id, players[id].last_command, players[id].last_params, players, rooms, gameitems, npcs, beastiary, monsterInstances, ticks, cursor, conn, mud)

	elif command == "self":
		Self(id, params, players, mud)
		DisplayPrompt(id, players, mud)

	elif command == "":
		DisplayPrompt(id, players, mud)

	else:																		# unknown command
		mud.send_message(id, "Unknown command: '{}'".format(command.upper()))
		DisplayPrompt(id, players, mud)