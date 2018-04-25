import time
from datetime import datetime

# define the Player class
class _Player:

	# BASIC
	name = 				None
	gender = 			None
	race = 				None
	description = 		"has not yet described themselves."
	room = 				None
	last_command = 		None
	last_params = 		None

	# AUTHENTICATION
	exist =				False
	authenticated =		False
	pw1 = 				None
	last_login = 		None
	created_on =		None
	playtime = 			datetime.strptime("00:00:00", "%H:%M:%S")
	
	# SKILLS
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

	# INVENTORY												
	inventory = 		list()
	bank = 				list()
	gold = 				0

	# EQUIPMENT
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

	# COMBAT
	in_combat = 		False
	balance = 			True
	fight_tick =		None
	totalstr = 			1
	totaldex =			1
	totalwis = 			1
	meleed = 			0
	ranged = 			0
	magicd = 			0
	hp =				30
	mp = 				10

	
	def __init__(self):
		pass
	