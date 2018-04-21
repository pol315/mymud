from classes.utilities import MakeProper
from classes.utilities import AdvertiseToRoom

def Emote(id, params, players, mud):
	AdvertiseToRoom(id, MakeProper("{} {}".format(players[id].name, params)), MakeProper("{} {}".format(players[id].name, params)), players, mud)