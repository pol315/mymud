def Compare(id, params, players, gameitems, mud):
	
	if (params.lower() in gameitems) and ((gameitems[params.lower()].__class__.__name__ == "_Weapon") or (gameitems[params.lower()].__class__.__name__ == "_Armor")):

		istr = gameitems[params.lower()].strength
		idex = gameitems[params.lower()].dexterity
		iwis = gameitems[params.lower()].wisdom
		imed = gameitems[params.lower()].meleed
		irad = gameitems[params.lower()].ranged
		imad = gameitems[params.lower()].magicd

		estr = 0
		edex = 0
		ewis = 0
		emed = 0
		erad = 0
		emad = 0

		if gameitems[params.lower()].__class__.__name__ == "_Weapon":
			if players[id].weapon1:
				estr = gameitems[players[id].weapon1].strength
				edex = gameitems[players[id].weapon1].dexterity
				ewis = gameitems[players[id].weapon1].wisdom
				emed = gameitems[players[id].weapon1].meleed
				erad = gameitems[players[id].weapon1].ranged
				emad = gameitems[players[id].weapon1].magicd

			mud.send_message(id, "Compared to your main hand weapon \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].weapon1), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			estr = 0
			edex = 0
			ewis = 0
			emed = 0
			erad = 0
			emad = 0

			if players[id].weapon2:
				estr = gameitems[players[id].weapon2].strength
				edex = gameitems[players[id].weapon2].dexterity
				ewis = gameitems[players[id].weapon2].wisdom
				emed = gameitems[players[id].weapon2].meleed
				erad = gameitems[players[id].weapon2].ranged
				emad = gameitems[players[id].weapon2].magicd

			mud.send_message(id, "Compared to your off-hand item \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].weapon2), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))



		elif gameitems[params.lower()].__class__.__name__ == "_Armor":
			if gameitems[params.lower()].slot == "chest":
				if players[id].chest:
					estr = gameitems[players[id].chest].strength
					edex = gameitems[players[id].chest].dexterity
					ewis = gameitems[players[id].chest].wisdom
					emed = gameitems[players[id].chest].meleed
					erad = gameitems[players[id].chest].ranged
					emad = gameitems[players[id].chest].magicd

				mud.send_message(id, "Compared to your chest armor \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].chest), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			elif gameitems[params.lower()].slot == "helmet":
				if players[id].helmet:
					estr = gameitems[players[id].helmet].strength
					edex = gameitems[players[id].helmet].dexterity
					ewis = gameitems[players[id].helmet].wisdom
					emed = gameitems[players[id].helmet].meleed
					erad = gameitems[players[id].helmet].ranged
					emad = gameitems[players[id].helmet].magicd

				mud.send_message(id, "Compared to your helmet \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].helmet), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			elif gameitems[params.lower()].slot == "legs":
				if players[id].legs:
					estr = gameitems[players[id].legs].strength
					edex = gameitems[players[id].legs].dexterity
					ewis = gameitems[players[id].legs].wisdom
					emed = gameitems[players[id].legs].meleed
					erad = gameitems[players[id].legs].ranged
					emad = gameitems[players[id].legs].magicd

				mud.send_message(id, "Compared to your leg armor \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].legs), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			elif gameitems[params.lower()].slot == "cloak":
				if players[id].cloak:
					estr = gameitems[players[id].cloak].strength
					edex = gameitems[players[id].cloak].dexterity
					ewis = gameitems[players[id].cloak].wisdom
					emed = gameitems[players[id].cloak].meleed
					erad = gameitems[players[id].cloak].ranged
					emad = gameitems[players[id].cloak].magicd

				mud.send_message(id, "Compared to your cloak \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].cloak), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			elif gameitems[params.lower()].slot == "gloves":
				if players[id].gloves:
					estr = gameitems[players[id].gloves].strength
					edex = gameitems[players[id].gloves].dexterity
					ewis = gameitems[players[id].gloves].wisdom
					emed = gameitems[players[id].gloves].meleed
					erad = gameitems[players[id].gloves].ranged
					emad = gameitems[players[id].gloves].magicd

				mud.send_message(id, "Compared to your gloves \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].gloves), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			elif gameitems[params.lower()].slot == "boots":
				if players[id].boots:
					estr = gameitems[players[id].boots].strength
					edex = gameitems[players[id].boots].dexterity
					ewis = gameitems[players[id].boots].wisdom
					emed = gameitems[players[id].boots].meleed
					erad = gameitems[players[id].boots].ranged
					emad = gameitems[players[id].boots].magicd

				mud.send_message(id, "Compared to your boots \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].boots), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			elif gameitems[params.lower()].slot == "ring":
				if players[id].ring:
					estr = gameitems[players[id].ring].strength
					edex = gameitems[players[id].ring].dexterity
					ewis = gameitems[players[id].ring].wisdom
					emed = gameitems[players[id].ring].meleed
					erad = gameitems[players[id].ring].ranged
					emad = gameitems[players[id].ring].magicd

				mud.send_message(id, "Compared to your ring \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].ring), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

			elif gameitems[params.lower()].slot == "necklace":
				if players[id].necklace:
					estr = gameitems[players[id].necklace].strength
					edex = gameitems[players[id].necklace].dexterity
					ewis = gameitems[players[id].necklace].wisdom
					emed = gameitems[players[id].necklace].meleed
					erad = gameitems[players[id].necklace].ranged
					emad = gameitems[players[id].necklace].magicd

				mud.send_message(id, "Compared to your necklace \"{}\", this item will alter your bonuses as such: {:+} strength, {:+} dexterity, {:+} wisdom, {:+} melee defence, {:+} ranged defence, {:+} magic defence".format(str(players[id].necklace), (istr - estr), (idex - edex), (iwis - ewis), (imed - emed), (irad - erad), (imad - emad)))

	else:
		mud.send_message(id, "This item cannot be compared.")
			