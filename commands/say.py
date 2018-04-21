from classes.utilities import MakeProper
from classes.utilities import AdvertiseToRoom

def Say(id, params, players, mud):
	AdvertiseToRoom(id, "{} says \"{}\"".format(players[id].name, MakeProper(params)), "You say \"{}\"".format(MakeProper(params)), players, mud)