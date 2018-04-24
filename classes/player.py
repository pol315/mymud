import time
from datetime import datetime

# define the Player class
class _Player:
	name = 				None
	gender = 			None
	exist =				False
	authenticated =		False
	pw1 = 				None
	race = 				None
	description = 		"has not yet described themselves."
	room = 				None
	last_login = 		None
	created_on =		None
	playtime = 			datetime.strptime("00:00:00", "%H:%M:%S")
	last_command = 		None
	last_params = 		None
	strength = 			1												# melee damage
	dexterity = 		1												# ranged damage
	wisdom = 			1												# magic damage
	endurance =			1												# determines HP
	clarity = 			1												# determines MP
	mining = 			1
	fishing = 			1
	foresting = 		1
	cooking = 			1
	blacksmithing = 	1												# plate and weapon making
	rangership =		1												# TBD.. bow making and leatherworking
	energycraft = 		1												# robe and magical item making
	strengthxp =		0												
	dexterityxp = 		0												
	wisdomxp = 			0												
	endurancexp =		0												
	clarityxp =			0												
	miningxp = 			0
	fishingxp =			0
	forestingxp = 		0
	cookingxp =			0
	blacksmithingxp = 	0												
	rangershipxp =		0												
	energycraftxp =		0												
	inventory = 		list()
	bank = 				list()
	gold = 				0
	helmet =			None
	chest = 			None
	legs = 				None
	gloves = 			None
	boots = 			None
	cloak = 			None
	necklace = 			None
	ring = 				None
	weapon1 = 			None
	weapon2 = 			None
	in_combat = 		False
	balance = 			True
	fight_tick =		None
	meleed = 			0
	ranged = 			0
	magicd = 			0
	
	def __init__(self):
		pass
	