#!/usr/bin/python3.8
# -*-coding:Utf-8 -*


import os
import pickle
os.chdir("package")

from package.class_mastermind import Mastermind

class Save:
	"""
	Attributs and methods about the saves file and scores.
	"""
	def __init__(self):
		self.scoreboard = {}	
		self.player_score = 0
		self.name = "name"

	def set_name(self, name):
		self.name = name
		
	def create_backup_file(self):
		"""
		This function checks that the "backups" file exists
		if not, it creates the "backup" file with an empty scoreboard.
		"""
		if not os.path.exists("saves"):
			with open("saves", "wb") as file:				
				my_pickler = pickle.Pickler(file)
				my_pickler.dump(self.scoreboard)				

	def write_backup(self, score):
		"""
		Creates a backup on behalf of the player with 0 points.
		"""
		with open("saves", "wb") as file:			
			my_pickler = pickle.Pickler(file)			
			self.player_score = score
			self.scoreboard[self.name] = self.player_score
			my_pickler.dump(self.scoreboard)			
			return self.player_score

	def open_backup(self):
		"""
		This methode opens the "backups" file
		then verify that the player has a save in his name.
		if so, it returns the player's score.
		if not, it calls write_backup().
		"""
		with open("saves", "rb") as file:
			my_depickler = pickle.Unpickler(file)
			self.scoreboard = my_depickler.load()
			for player, point in self.scoreboard.items():
				if player == self.name:
					self.player_score = point
					return self.player_score
			self.player_score = self.write_backup(0)
			return self.player_score

	def save_score(self, score):
		"""
		The function checks if the player's score is higher than his former 
		best score.
		If so, it overwrites the old score and records the new best score.
		if not, it does not touch the backup file.
		"""
		str_2 = str(self.player_score)
		str_3 = "You beat your old score! \nYou had "
		str_4 = " point(s) and now you have "
		str_5 = " point(s).\nScore saved.\n"
		str_6 = "You have matched your old score! \nYou have "
		str_7 = " point(s).\n"
		str_8 = "Your best score is : "
		str_9 = "\n"

		for player, point in self.scoreboard.items():
			# get the player's old score.
			if player == self.name:
				old_score = point
				str_1 = str(old_score)
				# If the player beats her/his old score.
				if old_score < score:
					self.write_backup(score)
					str_2 = str(self.player_score)
					text = str_3 + str_1 + str_4 + str_2 + str_5
				# If the player's old score is similar to her/his new score.
				elif old_score == self.player_score:
					text = str_6 + str_2 + str_7
				# I the player's old score is better than his/her new score.					
				else:
					text = str_8 + str_1 + str_9												
		return text
	
	def compare_score(self):
		"""
		Checks if the player's score is higher than his former 
		best score.
		If so, it overwrites the old score and records the new best score.
		if not, it does not touch the backup file.
		"""
		best_score = 0	
		for player, point in self.scoreboard.items():
			if point > best_score:
				best_score = point
				best_player = player
		if best_score != 0:
			list = ["The best score is ", str(best_score), " and is owned by :\n"]
			
			for player, point in self.scoreboard.items():
				if best_score == point:
					list_2 = ["		-", str(player), "\n"]
					text = " ".join(list_2)
					list.append(text)

			if self.player_score == best_score :
				list_3 = ["\nYou have the highest score :", str(best_score),"! Bravo !"]
				text = " ".join(list_3)
				list.append(text)

			text = "".join(list)
			return text
		text = "Il n'y a pas encore de scores enregistrés."
		return text
