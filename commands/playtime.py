import time
from datetime import datetime

def Playtime(id, players, mud):
	
	d1 = datetime.strptime(str(players[id].last_login), "%Y-%m-%d %H:%M:%S")
	d2 = datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
	preplaytime = players[id].playtime
	sessiontime = d2 - d1
	totaltime = preplaytime + sessiontime
	tosend = datetime.strptime(str(totaltime), "%Y-%m-%d %H:%M:%S")
	
	#TODO days - starts at 1900-01-01 so printing %d give us 1 day....
	mud.send_message(id, "You've been playing for {}.".format(tosend.strftime("%H hours, %M minutes and %S seconds")))