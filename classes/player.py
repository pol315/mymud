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
	strength = 			0												# melee damage
	dexterity = 		0												# ranged damage
	wisdom = 			0												# magic damage
	endurance =			5												# determines HP
	clarity = 			5												# determines MP
	mining = 			0
	fishing = 			0
	foresting = 		0
	cooking = 			0
	blacksmithing =		0												# plate and weapon making
	rangership =		0												# TBD.. bow making and leatherworking
	energycraft = 		0												# robe and magical item making
	strengthxp =		0												
	dexterityxp = 		0												
	wisdomxp = 			0												
	endurancexp =		2937												
	clarityxp =			2937											
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
	bankgold = 			0

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
	combat_target =		None
	balance = 			True
	fight_tick =		None
	totalstr = 			1
	totaldex =			1
	totalwis = 			1
	meleed = 			0
	ranged = 			0
	magicd = 			0
	hp =				25
	ap = 				25
	attack_speed = 		20

	
	def __init__(self):
		pass
	