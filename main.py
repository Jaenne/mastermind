#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from package.fonctions_mastermind import *
from package.class_mastermind import Mastermind
from package.class_save import Save

"""
In Mastermind you have to find the code.
It was invented by Mordecai Meirowitz.
You have 12 tries.
The number of points depends on the number of tries remaining.
during a test you offer a 4 color code.
The code cannot be made up of blanks.
Normal level : The code cannot contain the same color more than once.
Hard level : The code may contain duplicates.
The game will answer which colors are in the code.
and which colors are in the right places.
colors in the code = (colors in the code - colors in the right place).
colors will be replaced by letters: A B C D E F H I
The right colors in the wrong place are symbolized by: X
The right colors in the right place are symbolized by: V
"""

print("Welcome to Mastermind.")
s = Save()# Calls class Save
s.create_backup_file()

leave = False
change_name = True

# Game loop.
while not leave:
	if change_name:
		name = input("What's your name ? ")
		s.set_name(name)
		score = s.open_backup()
		print ("Hello ", name, "\nYour best score :", score)		
		
	m = Mastermind()# Calls class Mastermind 
	mode = False
	while not mode:
		print(mode_text())
		choice = input("Enter your choice : ")
		mode, text = m.set_mode_choice(choice)
		print(text)

	# Generate code loop.
	generate_code = False
	while not generate_code:
		generate_code = m.set_genererate_code()

	print(m.display_help())
		
	# Secret code loop.
	while m.get_good_places() < 4 and m.get_tries_counter() < 12:
		# Try loop
		ok = False
		while not ok:
			entry = input("Enter your combination : ")
			ok = m.verify_entry(entry)
			if not ok:
				print("Your combination must contain 4 characters among allowed letters.")
		m.set_combination()
		m.set_color_comparison()
		m.set_places_comparison()
		print(m.display_result())
		
	score = (12 - m.get_tries_counter())
	
	if m.get_good_places() == 4:
		print(
			"\n\nCongratulations, you broke the code in",
			m.get_tries_counter(), 
			"tries.\n\nYour score is :",
			score
			)
		print(s.save_score(score))	
		
	else:
		code = m.get_code()
		code = " ".join(code)
		print(
			"\nYou did not break the code : \n		",
			code,
			"\n\nYour score is :",
			score,
			"\n"
			)
	
	print(s.compare_score())
	
	# Exit conform entry loop.
	conform_entry = False
	print(exit_text())
	while not conform_entry:		
		entry = input("Enter your choice, only one letter : ")
		leave, change_name, conform_entry = exit(entry)
		
