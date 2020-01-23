#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

"""
All the functions of the Mastermind.
"""

import os
import pickle
os.chdir("package")
"""
Menu functions --------------------------------------------------------------------
"""

def open_backup_file():
	"""
	This function checks that the "backups" file exists
	if not, it creates the "backup" file with an empty scoreboard.
	"""
	if not os.path.exists("saves"):
		with open("saves", "wb") as file:
			scoreboard = {}
			my_pickler = pickle.Pickler(file)
			scoreboard = my_pickler.dump(scoreboard)

def write_backup(name, scoreboard):
	with open("saves", "wb") as file:
		player_score = 0
		my_pickler = pickle.Pickler(file)
		scoreboard[name] = player_score
		scoreboard = my_pickler.dump(scoreboard)
		return player_score

def open_backup(name):
	"""
	This function opens the "backups" file
	then verify that the player has a save in his name.
	if so, it returns the player's score in the main function.
	if not, it will create a backup on behalf of the player with 0 points.
	"""
	with open("saves", "rb") as file:
		my_depickler = pickle.Unpickler(file)
		scoreboard = my_depickler.load()
		for player, point in scoreboard.items():
			if player == name:
				player_score = point
				return player_score
		player_score = write_backup(name, scoreboard)
		return player_score
    
def save_score(name, player_score):
	"""
	The function checks if the player's score is higher than his former 
	best score.
	If so, it overwrites the old score and records the new best score.
	if not, it does not touch the backup file.
	"""
	with open("saves", "rb") as file:
		my_depickler = pickle.Unpickler(file)
		scoreboard = my_depickler.load()
		for player, point in scoreboard.items():
			if player == name:
				old_score = point
				if old_score < player_score:
					with open("saves", "wb") as file:
						my_pickler = pickle.Pickler(file)
						scoreboard[name] = player_score
						scoreboard = my_pickler.dump(scoreboard)
						print(
							"You beat your old score! \nYou had", 
							old_score, "point(s) and now you have",
							 player_score, "point(s).\nScore saved.\n"
							 )
				elif old_score == player_score:
					print(
						"You have matched your old score! \nYou have",
						player_score, 
						"point(s).\n"
						)
				else:
					print(
						"Your best score is :", 
						old_score,
						"\n"
						)

def compare_score(name, player_score):
	"""
	The function checks if the player's score is higher than his former 
	best score.
	If so, it overwrites the old score and records the new best score.
	if not, it does not touch the backup file.
	"""
	best_score = 0
	with open("saves", "rb") as file:
		my_depickler = pickle.Unpickler(file)
		scoreboard = my_depickler.load()
		for player, point in scoreboard.items():
			if point > best_score:
				best_score = point
				best_player = player
			if best_score != 0:
				print("The best score is", best_score, "and is owned by :")
				for player, point in scoreboard.items():
					if best_score == point:
						print("		-", player)
				if player_score == best_score :
					print(
						"\nYou have the highest score :", 
						best_score,
						"! Congratulations !"
						)

def exit(name):
	phrase_1 = "\nTo quit hit Q.\n"
	phrase_2 = "To change player hit P.\n"
	phrase_3 = "To continue hit C.\n"
	phrase_4 = "Sorry I did not understand. Please try again."
	print(phrase_1 + phrase_2 + phrase_3)
	entry = input("Enter your choice, only one letter : ")
	if not entry.isalpha():
		print(phrase_4)
		return exit(name)
	entry = entry.capitalize()

	if entry == "Q":
		return True, name	
	elif entry == "P":
		name = input("What's your name ? ")
		open_backup_file(name)
		return False, name
	elif entry == "C":
		return False, name
	else:
		print(phrase_4)
		return exit(name)


