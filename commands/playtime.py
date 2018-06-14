import time
import math
import datetime

def Playtime(id, players, ticks, mud):
	
	totalsecondsplayed = players[id].playtime + math.floor((ticks - players[id].auth_tick) / 5)
	
	mud.send_message(id, "You've been playing for {!s:0>8}.".format(datetime.timedelta(seconds=totalsecondsplayed)))