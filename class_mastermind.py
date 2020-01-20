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

	def set_combination(self):
		""" 
		The player must enter 4 letters.
		These letters are stored in the authorized list.		
		If the entry is not suitable, because there are too many characters
		or that they are not alpha characters, the function
		start over at the beginning.		
		The entry is converted capitals.		
		If the entry is not suitable, because the letters are not
		not in the authorized list, print each forbidden letter,
		the function starts again at beginning.		
		Else : Each letter of the entry is stored in the list
		combination.
		"""
		ok = True
		entry = input(
			"Enter your combination : "
			)
		if len(entry) != 4 or not entry.isalpha():
			print(
				"Your combination must contain 4 characters among allowed letters."
				)
			return self.set_combination()
		else :
			entry = (entry).upper()
			for index, letter in enumerate(entry):
				if entry[index] not in self.allowed:
					print(entry[index], "is not allowed.")
					ok = False
				else:
					self.combination[index] = entry[index]
			if not ok:
				return self.set_combination()
						
	def set_genererate_code_whithout_duplicates(self):
		""" 
		The code is a list of 4 "x".
		Each x takes a value between 0 and 7.
		If there is a double, the function starts again from the beginning.
		When the code contains only numbers,
		Each number is converted into a letter among those
		authorized.
		Each letter is saved in self.code.
		"""
		for index, element in enumerate(self.code):
			number = str(randrange(8))
			if number in self.code:
				return self.set_genererate_code_whithout_duplicates()
			else :
				self.code[index] = number
		for i, contenu in enumerate(self.code):
			if contenu == "0":
				self.code[i] = self.allowed[0]
			elif contenu == "1":
				self.code[i] = self.allowed[1]
			elif contenu == "2":
				self.code[i] = self.allowed[2]
			elif contenu == "3":
				self.code[i] = self.allowed[3]
			elif contenu == "4":
				self.code[i] = self.allowed[4]
			elif contenu == "5":
				self.code[i] = self.allowed[5]
			elif contenu == "6":
				self.code[i] = self.allowed[6]
			else:
				self.code[i] = self.allowed[7]
		
	def set_genererate_code(self):
		""" 
		The code is a list of 4 "x".
		Each x takes a value between 0 and 7.
		Each number is converted into a letter among those
		authorized.
		Each letter is saved in self.code.
		"""		
		for index, element in enumerate(self.code):
			n = str(randrange(8))
			self.code[index] = n
		for i, contenu in enumerate(self.code):
			if contenu == "0":
				self.code[i] = self.allowed[0]
			elif contenu == "1":
				self.code[i] = self.allowed[1]
			elif contenu == "2":
				self.code[i] = self.allowed[2]
			elif contenu == "3":
				self.code[i] = self.allowed[3]
			elif contenu == "4":
				self.code[i] = self.allowed[4]
			elif contenu == "5":
				self.code[i] = self.allowed[5]
			elif contenu == "6":
				self.code[i] = self.allowed[6]
			else:
				self.code[i] = self.allowed[7]

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

	def display_result(self):
		self.good_colors = (self.good_colors - self.good_places)
		"""
		Displays in 1 line informations necessary 
		for the resolution of the code.
		"""
		print(
			"X :", self.good_colors, 
			"				",
			self.combination[0], 
			self.combination[1], 
			self.combination[2], 
			self.combination[3], 
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

	def display_help(self):		
		phrase_1 = "X means : good color but BAD place.\n"
		phrase_2 = "V means : good color and GOOD place.\n"	
		phrase_3 = "You have 12 tries.\n"	
		print(phrase_1 + phrase_2 + phrase_3)
		print(
			"\n\nBAD place(s)", 
			"	",
			"Allowed letters : ",
			self.allowed[0],
			self.allowed[1],
			self.allowed[2],
			self.allowed[3],
			self.allowed[4],
			self.allowed[5],
			self.allowed[6],
			self.allowed[7],
			"	",
			"GOOD place(s)\n", 
			)
