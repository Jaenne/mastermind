#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from package.fonctions_mastermind import *
from package.classe_mastermind import Mastermind

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
name = input("What's your name ? ")

# Ouvrir le fichier score.
open_backup_file()
score = open_backup(name)
leave = False

# Boucle de jeu.
while not leave:
	m = Mastermind()
	mode = mode_choice()

	if mode == "duplicates":
		m.set_genererate_code()
		print("\nThe code consists of 4 letters. There may be duplicates.")
	else:
		m.set_genererate_code_whithout_duplicates()	
		print("\nThe code consists of 4 letters, without duplicates.")

	m.display_help()
	
	# Secret code loop.
	while m.get_good_places() < 4 and m.get_tries_counter() < 12:
		m.set_combination()
		m.set_color_comparison()
		m.set_places_comparison()
		m.display_result()
		
	score = (12 - m.get_tries_counter())
	
	if m.get_good_places() == 4:
		print(
			"\n\nCongratulations, you broke the code in",
			m.get_tries_counter(), 
			"tries.\nYour score is :",
			score
			)
		save_score(name, score)
		
	else:
		code = m.get_code()
		print(
			"\nYou did not break the code : \n		",
			code[0], 
			code[1], 
			code[2], 
			code[3], 
			"\nYour score is :",
			score
			)

	compare_score(name, score)

	leave, name = exit(name)
	quitter, nom = sortir(nom)
