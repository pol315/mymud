import os
import re

def Help(id, params, mud):
	if params:
		search = re.sub('[^A-Za-z]+', '', params).lower()
		if os.path.isfile("help/" + search):												# read file and send it line by line
			mud.send_message(id, "")
			with open("help/" + search, 'r') as fp:
				for line in enumerate(fp):
					mud.send_message(id, "{}".format(line[1].rstrip('\n').rstrip('\r')))
			
		else:																			# search files in directory and send back which contain the search term
			mud.send_message(id, "File \"" + search + "\" was not found. Looking for help files containing the word \"" + search + "\"...")
			for filename in os.listdir('help'):
				with open("help/" + filename, 'r') as fp:
					if search in fp.read().lower():
						mud.send_message(id, os.path.basename(fp.name).upper())
				
			mud.send_message(id, "End of search.")
			
			
	else:
		mud.send_message(id, "Try searching for a specific topic such as \"HELP LOOK\"")					