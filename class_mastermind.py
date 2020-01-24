#!/usr/bin/python3.8
# -*-coding:Utf-8 -*


from random import randrange

class Mastermind:
	"""
	Attributs and methods necessary to resolve the game.
	"""
	def __init__(self):
		self.allowed = ["A", "B", "C", "D", "E", "F", "G", "H"]
		self.combination = ["", "", "", ""]
		self.code = ["x", "x", "x", "x"]
		self.tries_counter = 0
		self.good_places = 0
		self.good_colors = 0
		self.mode_choice = "duplicates"
		self.entry = ""

	def set_mode_choice(self, choice):
		"""
		The entry is not a letter.

		Entry is upper.
		The mode choosed is with duplicates.
			set mode
		The mode choosed is without duplicates.
			set mode

		The entry is not "d" or "n"

		Each time, returns : 
			- mode : True if entry is conform or False if not conform.
			- and The text will be display.
		"""		
		str_1 = "Sorry I did not understand. Please try again."
		str_2 = "\nThe code consists of 4 letters. There may be duplicates."
		str_3 = "\nThe code consists of 4 letters, without duplicates."
		
		if not choice.isalpha():
			text = str_1
			mode = False

		choice = choice.upper()
		if choice == "D":
			self.mode_choice = "duplicates"
			text = str_2
			mode = True			
		elif choice == "N":
			self.mode_choice = "not_duplicates"
			text = str_3
			mode = True

		else :
			text = str_1
			mode = False

		return mode, text
	
	def set_combination(self):
		"""
		the entry is converted capitals.
		Each letter of the entry is stored in the list
		combination.
		"""
		self.entry = (self.entry).upper()
		for index, letter in enumerate(self.entry):
			self.combination[index] = self.entry[index]
								

	def verify_entry(self, entry):
		""" 
		Entry must contains 4 letters.
		These letters are stored in the authorized list.		
		If the entry is suitable : 
			- returns True ;
			- set entry.
		If the entry is not suitable, because there are too many characters
		or because the upper letters are not in the authorized list : 
			- returns False.
		"""
		# Thank you Julien00859 !
		if len(entry) == 4 and all(char in self.allowed for char in entry.upper()):
			self.entry = entry			
			return True
		else :						
			return False
	
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
		If mode choosed is "not_duplicates" And if there is a double :
			- returns False
		Else :
			- the function convert_code is called;
			- returns True
		"""		
		for index, element in enumerate(self.code):
			number = str(randrange(8))
			self.code[index] = number
			element = number
			if self.mode_choice == "not_duplicates" and self.code.count(element) > 1:				
				return False			
		self.convert_code()
		return True

	def set_color_comparison(self):
		""" 
		Compares the code and the combination by looking
		for color matches.
		Duplicates the combination in backup_combination;
		For each element in backup_combination :
			For each letter in code:
				if the backup_combination letter has more occurrences  
				than the same letter in the code:
					- Replaces excess occurrences in backup_combination 
					with an "x";
			if letter in backup_combination is in the code :
				- increments self.good_colors by 1.
		Increments the test counter by 1.
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
		Searches for well-placed colors:
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
		Help text about the game.
		"""		
		str_1 = "X means : good color but BAD place.\n"
		str_2 = "V means : good color and GOOD place.\n"	
		str_3 = "You have 12 tries.\n"
		str_4 = "\n\nBAD place(s)"
		str_5 = "	"
		str_6 = "Allowed letters : "
		str_7 = string_allowed = " ".join(self.allowed)
		str_8= "GOOD place(s)\n"

		text = (str_1+str_2+str_3+str_4+str_5+str_6+str_7+str_5+str_8)
		return text

	def display_result(self):		
		"""
		Text : displays in 1 line informations necessary 
		for the resolution of the code.
		"""
		self.good_colors = (self.good_colors - self.good_places)
		str_1 = "X : "
		str_2 = str(self.good_colors)
		str_3 = "				"
		str_4 = " ".join(self.combination)
		str_5 = "V : "
		str_6 = str(self.good_places)
		str_7 = "		"
		str_8 = "try : "
		str_9 = str(self.tries_counter)
		
		text = str_1+str_2+str_3+str_4+str_3+str_5+str_6+str_7+str_8+str_9
		return text

	def get_good_places(self):
		return self.good_places

	def get_tries_counter(self):
		return self.tries_counter

	def get_code(self):
		return self.code
