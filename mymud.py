#!/usr/bin/env python

import sys
sys.path.append('areas')
sys.path.append('classes')
sys.path.append('commands')
sys.path.append('help')
sys.path.append('items')
sys.path.append('server')

from classes.authentication import CreateNewUser
from classes.authentication import LogPlayerIn
from classes.authentication import ValidateName
from classes.combat			import ForgetTargets
from classes.combat			import RegainBalance
from classes.combat			import MonsterAttacks
from classes.combat			import RespawnMonsters
from classes.parsecommand	import ParseCommand
from classes.utilities		import PlacePlayerInGame
from classes.utilities		import ParseRooms
from classes.utilities		import ParseGameItems
from classes.utilities		import ParseNPCs
from classes.utilities		import ParseMonsters
from classes.utilities		import PlaceMonstersInRooms
from classes.utilities		import CleanUpDeadPlayers

from classes.player   		import _Player
from classes.server 		import _Server
from classes.room	 		import _Room
from classes.roomitem 		import _RoomItem
from classes.gameitem 		import _GameItem
from classes.gameitem 		import _Weapon
from classes.gameitem 		import _Armor
from classes.npc	 		import _NPC
from classes.monster 		import _Monster

from configparser 	  		import SafeConfigParser

import psycopg2
import json
import time

config = SafeConfigParser()
config.read('config.ini')
dbpass = config.get('Database', 'Password')

# connect to the database
conn_string = "host='jasonhiggins.ca' port='9989' dbname='mymud_db' user='postgres' password='" + dbpass + "'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

rooms = ParseRooms()				# structure defining the rooms in the game - loaded from a json file
gameitems = ParseGameItems()
npcs = ParseNPCs()
beastiary = ParseMonsters()
monsterInstances = {}
deadMonsters = {}
PlaceMonstersInRooms(rooms, beastiary, monsterInstances)
players = {}												# stores the players in the game
ticks = 0													# stores how many ticks have gone by since server start

TICK_SPEED = 0.2

mud = _Server()												# start the server

while True:													# main game loop. We loop forever (i.e. until the program is terminated)

	time.sleep(TICK_SPEED)									# pause for the tick speed on each loop, so that we don't constantly use 100% CPU time
	ticks = ticks + 1
	mud.update()											# 'update' must be called in the loop to keep the game running and give us up-to-date information

	RegainBalance(players, monsterInstances, ticks, mud) 	# go through all players and monsters and see if they are ready to fight again
	MonsterAttacks(players, monsterInstances, ticks, mud)	# if a monster is ready to attack and has a target
	CleanUpDeadPlayers(players, gameitems, rooms, monsterInstances, cursor, conn, mud)	# RIP
	ForgetTargets(monsterInstances, ticks)					# if a player dies or is away for a set period of time, monsters forget them as a target
	RespawnMonsters(monsterInstances, deadMonsters, beastiary, ticks, players, mud)

	for id in mud.get_new_players():						# go through any newly connected players

		players[id] = _Player()

		mud.send_message(id, "+-----------------------------------------------+", mud._BOLD, mud._RED)
		mud.send_message(id, "|              Welcome to MyMud!                |", mud._BOLD, mud._RED)
		mud.send_message(id, "|     A land of whimsical adventure and fun.    |", mud._BOLD, mud._RED)
		mud.send_message(id, "|                                               |", mud._BOLD, mud._RED)
		mud.send_message(id, "|              Enjoy your stay!                 |", mud._BOLD, mud._RED)
		mud.send_message(id, "+-----------------------------------------------+", mud._BOLD, mud._RED)
		mud.send_message(id, "")
		mud.send_message(id, "")
		mud.send_message(id, "What is your name?")			# send the new player a prompt for their name

	for id in mud.get_disconnected_players():				# go through any recently disconnected players
		if id not in players:								# if for any reason the player isn't in the player map, skip them and move on to the next one
			continue

		for pid, pl in players.items():																# go through all the players in the game
			mud.send_message(pid, "{} has vanished from the world.".format(players[id].name))	# send each player a message to tell them about the disconnected player

		del(players[id])									# remove the player's entry in the player dictionary

	for id, command, params in mud.get_commands():			# go through any new commands sent from players
		if id not in players:								# if for any reason the player isn't in the player map, skip them and move on to the next one
			continue
		
		ParseCommand(id, command.lower(), params.strip(), players, rooms, gameitems, npcs, beastiary, monsterInstances, deadMonsters, ticks, cursor, conn, mud)
		
			