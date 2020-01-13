#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from package.fonctions_mastermind import *
import os
os.chdir(".")

"""
Dans Mastermind vous devez trouver le code.
Il fut inventé par Mordecai Meirowitz.
Vous avez 12 essais.
Le nombre de points dépend du nombre d'essais restant.
lors d'un essai vous proposez un code de 4 couleur.
Le code ne peut pas contenir plusieurs fois la même couleur.
Le code ne peut être composé de vide.
Le jeu repondra quelles couleurs sont bien dans le codes
et quelles couleurs sont à la bonnes places.
couleurs dans le codes = (couleurs dans le code - couleurs à la bonne place).
les couleurs seront remplacées par des lettres : A B C D E F H I
Les bonnes couleurs à la mauvaise place sont symbolisées par : X
Les bonnes couleurs à la bonne place sont symbolisées par : V
"""

# Message d'accueil.
print("Bienvenue dans Mastermind.")
nom = input("Quel est votre nom ? ")
phrase_1 = "X signifie : bonne couleur MAL placée.\n"
phrase_2 = "V signifie : bonne couleur BIEN placée.\n"
phrase_3 ="Le code se compose de 4 lettres, sans doublons.\n"
phrase_4 = "Vous avez 12 essais.\n"
print(phrase_1 + phrase_2 + phrase_3 + phrase_4)

# Ouvrir le fichier score.
tableau_des_scores = ouvrir_le_fichier_sauvegardes()
score = ouvrir_la_sauvegarde(nom)
print("Votre meilleur score :", score)
print(
	"\n\nX : MAL placée(s)", 
	"				",
	"V : BIEN placée(s)\n", 
	)

quitter = False

# Boucle de jeu.
while not quitter:
	compteur_d_essais = 0
	bonnes_places = 0
	compteur_d_essais = 0
	code = generer_code_sans_doubles()
	#print("Code sans doubles :\n", code)

	# Boucle du code en cours de cassage.
	while bonnes_places < 4 and compteur_d_essais < 12:
		combinaison = verifier_saisie()
		bonnes_couleurs, compteur_d_essais, combinaison = comparaison_couleurs(
																combinaison, 
																code, 
																compteur_d_essais
																)
		tableau_code = transformer_en_tableau(code)
		tableau_combinaison = transformer_en_tableau(combinaison)
		#afficher_tableau(tableau_code, "code")
		#afficher_tableau(tableau_combinaison, "combinaison")
		bonnes_places = comparaison_places(
							tableau_combinaison, 
							tableau_code 
							)
		bonnes_couleurs = (bonnes_couleurs - bonnes_places)

		# Affiche en 1 ligne les informations nécessaires à la résolution du code.
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
			"Félictations, vous avez cassé le code en ",
			compteur_d_essais, 
			"essais.\n Votre score est :",
			score
			)
		enregistrer_le_score(nom, score)
	else:
		print(
			"Vous n'avez pas cassé le code : \n		",
			code[0], 
			code[1], 
			code[2], 
			code[3], 
			"\nVotre score est :",
			score
			)

	quitter = sortir()
