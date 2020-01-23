#!/usr/bin/python3.8
# -*-coding:Utf-8 -*


from random import randrange

class Mastermind:
	def __init__(self):
		self.allowed = ["A", "B", "C", "D", "E", "F", "G", "H"]
		self.combination = ["", "", "", ""]
		self.code = ["x", "x", "x", "x"]
		self.tries_counter = 0
		self.good_places = 0
		self.good_colors = 0
		self.mode_choice = "duplicates"

	def set_mode_choice(self):
		phrase_1 = "\nChoose your mode :\n"
		phrase_2 = "Hit D to play with duplicates in code.\n"
		phrase_3 = "Hit N to play without duplicates in code."
		phrase_4 = "Sorry I did not understand. Please try again."
		print(phrase_1 + phrase_2 + phrase_3)

		choice = input("Enter your choice : ")
		if not choice.isalpha():
			print(phrase_4)
			return self.set_mode_choice()
		choice = choice.capitalize()
		if choice == "D":
			self.mode_choice = "duplicates"
			print("\nThe code consists of 4 letters. There may be duplicates.")
		elif choice == "N":
			self.mode_choice = "not_duplicates"
			print("\nThe code consists of 4 letters, without duplicates.")
		else :
			print(phrase_4)
			return self.set_mode_choice()		

	def set_combination(self, entry):
		""" 
		Entry must contains 4 letters.
		These letters are stored in the authorized list.		
		If the entry is suitable, the entry is converted capitals.
		Each letter of the entry is stored in the list
		combination.
		If the entry is not suitable, because there are too many characters
		or because the upper letters are not in the authorized list, the 
		function starts over at the beginning.
		"""
		# Thank you Julien00859
		while True:			
			if len(entry) == 4 and all(char in self.allowed for char in entry.upper()):
				entry = (entry).upper()
				for index, letter in enumerate(entry):
					self.combination[index] = entry[index]
				break
			print("Your combination must contain 4 characters among allowed letters.")
				
						
	def convert_code(self):
		"""
		Each number is converted into a letter among those
		authorized.
		Each letter is saved in self.code.
		"""
		for i, contenu in enumerate(self.code):
			# Thank you Linek !
			self.code[i] = self.allowed[int(contenu)]
			print(self.code)
								
	def set_genererate_code(self):
		""" 
		The code is a list of 4 "x".
		Each x takes a value between 0 and 7.
		If mode choosed is "not_duplicates":
			If there is a double, the function starts again from the beginning.
		Else, the function convert_code is called.
		"""		
		for index, element in enumerate(self.code):
			number = str(randrange(8))
			self.code[index] = number
			element = number
			if self.mode_choice == "not_duplicates":
				if self.code.count(element) > 1:
					return self.set_genererate_code()
		self.convert_code()

	def set_color_comparison(self):
		""" 
		Compares the code and the combination by looking
		for color matches.
		- duplicates the combination in backup_combination;
		For each letter in backup_combination :
			if the backup_combination letter has more occurrences  
			than the same letter in the code:
				- Replaces excess occurrences in backup_combination 
				with an "x";
		- compare the backup_combination with the code;
		- increments the test counter by 1.
		"""
		self.good_colors = 0
		backup_combination = []
		backup_combination.extend(self.combination)
		for i, element in enumerate(backup_combination):
			for index, letter in enumerate(self.code):								
				if backup_combination.count(element) > self.code.count(letter):					
					if element == letter:					
						del backup_combination[i]
						backup_combination.insert(i, "x")									
			if backup_combination[i] in self.code:
				self.good_colors += 1		
		self.tries_counter += 1
						
	def set_places_comparison(self):
		"""
		Function that searches for well-placed colors:
		Compares the colors for each similar index of the
		combination list and code list.
		saves the number of well-placed colors in good_places. 
		"""
		self.good_places = 0
		for i, element in enumerate(self.combination):
			for index, letter in enumerate(self.code):
				if i == index:
					if element == letter:
						self.good_places +=1

	def display_help(self):
		"""
		Displays help about game.
		"""		
		phrase_1 = "X means : good color but BAD place.\n"
		phrase_2 = "V means : good color and GOOD place.\n"	
		phrase_3 = "You have 12 tries.\n"
		string_allowed = " ".join(self.allowed)
		print(phrase_1 + phrase_2 + phrase_3)
		print(
			"\n\nBAD place(s)", 
			"	",
			"Allowed letters :",
			string_allowed,
			"	",
			"GOOD place(s)\n", 
			)

	def display_result(self):
		self.good_colors = (self.good_colors - self.good_places)
		"""
		Displays in 1 line informations necessary 
		for the resolution of the code.
		"""
		string_conbination = " ".join(self.combination)
		print(
			"X :", self.good_colors, 
			"				",
			string_conbination, 
			"			",
			"V :", self.good_places, 
			"		",
			"try n°", self.tries_counter
			)

	def get_good_places(self):
		return self.good_places

	def get_tries_counter(self):
		return self.tries_counter

	def get_code(self):
		return self.code


