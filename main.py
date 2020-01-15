#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from package.fonctions_mastermind import *
import os
os.chdir(".")

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
nom = input("What's your name ? ")
print(message_accueil())

# Ouvrir le fichier score.
tableau_des_scores = ouvrir_le_fichier_sauvegardes()
score = ouvrir_la_sauvegarde(nom)

quitter = False

# Boucle de jeu.
while not quitter:
	compteur_d_essais = 0
	bonnes_places = 0
	compteur_d_essais = 0
	print("Choose your difficulty level.")
	difficulte = choix_difficulte()

	if difficulte == "hard":
		code = generer_code()
		#print("Code :\n", code)
		print("The code consists of 4 letters. There may be duplicates.")
	else:
		code = generer_code_sans_doubles()	
		#print("Code sans doubles :\n", code)
		print("The code consists of 4 letters, without duplicates.\n")

	print(
		"\n\nX : BAD place(s)", 
		"				",
		"V : GOOD place(s)\n", 
		)

	# Secret code loop.
	while bonnes_places < 4 and compteur_d_essais < 12:
		combinaison = verifier_saisie()
		bonnes_couleurs, compteur_d_essais, combinaison = comparaison_couleurs(
										combinaison, 
										code, 
										compteur_d_essais
										)
		bonnes_places = comparaison_places(combinaison, code)
		bonnes_couleurs = (bonnes_couleurs - bonnes_places)

		# Displays in 1 line the information necessary 
		# for the resolution of the code.
		print(
			"X :", bonnes_couleurs, 
			"			",
			combinaison[0], 
			combinaison[1], 
			combinaison[2], 
			combinaison[3], 
			"			",
			"V :", bonnes_places, 
			"		",
			"try n°", compteur_d_essais
			)
	if difficulte == "hard":
		score = (12 - compteur_d_essais) * 2
	else:
		score = (12 - compteur_d_essais)

	if bonnes_places == 4:
		print(
			"\n\nCongratulations, you broke the code in",
			compteur_d_essais, 
			"tries.\nYour score is :",
			score
			)
		enregistrer_le_score(nom, score)
	else:
		print(
			"You did not break the code : \n		",
			code[0], 
			code[1], 
			code[2], 
			code[3], 
			"\nYour score is :",
			score
			)

	quitter, nom = sortir(nom)
