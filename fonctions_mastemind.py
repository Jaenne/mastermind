#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

"""
Functions what are not useful to resolve the game or to manage the saves file or scores.
"""


def mode_text():
	phrase_1 = "\nChoose your mode :\n"
	phrase_2 = "Hit D to play with duplicates in code.\n"
	phrase_3 = "Hit N to play without duplicates in code."
	
	text = phrase_1 + phrase_2 + phrase_3
	return text

def exit_text():
	phrase_1 = "\nTo quit hit Q.\n"
	phrase_2 = "To change player hit P.\n"
	phrase_3 = "To continue hit C.\n"	

	text = phrase_1 + phrase_2 + phrase_3
	return text

def exit(entry):
	"""
	Test if the entry is not a letter. 
	
	The player wants leave;
	The player wants to change name.
	The player wants continue with same settings;
	
	The entry is not in allowed choices.

	Each time : returns : leave, change_name, conform_entry.
	"""	
	if not entry.isalpha():
		return False, False, False
	
	entry = entry.capitalize()
	# The player wants leave.
	if entry == "Q":		
		return True, False, True
	# The player wants to change name.	
	elif entry == "P":
		return False, True, True
	# The player wants continue with same settings.
	elif entry == "C":
		return False, False, True

	# The entry is not in allowed choices.
	else:
		return False, False, False


