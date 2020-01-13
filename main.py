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
During a test you offer a 4 color code.
The code cannot contain the same color more than once.
The code cannot be made up of blanks.
The game will answer which colors are in the codes
and which colors are in the right places.
Colors in the code = (colors in the code - colors in the right place).
Colors will be replaced by letters: A B C D E F H I
The right colors in the wrong place are symbolized by: X
The right colors in the right place are symbolized by: V

"""

# Welcome text :
print("Welcome in Mastermind.")
nom = input("What's your name ? ")
phrase_1 = "X means : right color BAD place.\n"
phrase_2 = "V means : right color Good place.\n"
phrase_3 ="The code consists of 4 letters, without duplicates.\n"
phrase_4 = "You have 12 tries.\n"
print(phrase_1 + phrase_2 + phrase_3 + phrase_4)

# Open the score file.
tableau_des_scores = ouvrir_le_fichier_sauvegardes()
score = ouvrir_la_sauvegarde(nom)
print("Your best score :", score)
print(
	"\n\nX : BAD place(s)", 
	"				",
	"V : GOOD place(s)\n", 
	)

quitter = False

# Game loop.
while not quitter:
	compteur_d_essais = 0
	bonnes_places = 0
	compteur_d_essais = 0
	code = generer_code_sans_doubles()
	#print("Code :\n", code)

	# Secret code loop.
	while bonnes_places < 4 and compteur_d_essais < 12:
		combinaison = verifier_saisie()
		bonnes_couleurs, compteur_d_essais, combinaison = comparaison_couleurs(
										combinaison, 
										code, 
										compteur_d_essais
										)
		tableau_code = transformer_en_tableau(code)
		tableau_combinaison = transformer_en_tableau(combinaison)
		bonnes_places = comparaison_places(
						tableau_combinaison, 
						tableau_code 
						)
		bonnes_couleurs = (bonnes_couleurs - bonnes_places)

		# Displays in 1 line informations necessary for the resolution of the code.
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
			"essai n°", compteur_d_essais
			)

	score = (12 - compteur_d_essais)

	if bonnes_places == 4:
		print(
			"Congratulations, you broke the code in : ",
			compteur_d_essais, 
			"tries.\n Your score is : ",
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

	quitter = sortir()
