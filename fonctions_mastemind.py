#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

"""
All the functions of the Mastermind.
"""

import os
import pickle
from random import randrange
os.chdir(".")
"""
Menu functions --------------------------------------------------------------------
"""
def ouvrir_le_fichier_sauvegardes():
	"""
	This function checks that the "backups" file exists
	if so, it returns the content in the main function.
	if not, it creates the "backup" file with an empty scoreboard.
	then it returns the content in the main function.
	"""
	if os.path.exists("sauvegardes"):
		with open("sauvegardes", "rb") as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			tableau_des_scores = mon_depickler.load()		
	else:
		with open("sauvegardes", "wb") as fichier:
			mon_pickler = pickle.Pickler(fichier)
			tableau_des_scores = {}
			tableau_des_scores = mon_pickler.dump(tableau_des_scores)
	return tableau_des_scores

def ouvrir_la_sauvegarde(nom_du_joueur):
	"""
	This function opens the "backups" file
	then verify that the player has a save in his name.
	if so, it returns the player's score in the main function.
	if not, it will create a backup on behalf of the player with 0 points.
	then returns the player's score in the main function.
	"""
	with open("sauvegardes", "rb") as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		tableau_des_scores = mon_depickler.load()
		for k, v in tableau_des_scores.items():
			if k == nom_du_joueur:
				score_du_joueur = v
				print ("Hello ", nom_du_joueur)
				print("Your best score :", score_du_joueur)
				return score_du_joueur
	with open("sauvegardes", "wb") as fichier:
		mon_pickler = pickle.Pickler(fichier)
		score_du_joueur = 0
		tableau_des_scores[nom_du_joueur] = score_du_joueur
		tableau_des_scores = mon_pickler.dump(tableau_des_scores)
	print ("Hello ", nom_du_joueur)		
	print("Your best score :", score_du_joueur)
	return score_du_joueur

def enregistrer_le_score(nom_du_joueur, score_du_joueur):
	"""
	The function checks if the player's score is higher than his former 
	best score.
	If so, it overwrites the old score and records the new best score.
	if not, it does not touch the backup file.
	"""
	with open("sauvegardes", "rb") as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		tableau_des_scores = mon_depickler.load()
		for k, v in tableau_des_scores.items():
			if k == nom_du_joueur:
				ancien_score = v
				if ancien_score < score_du_joueur:
					with open("sauvegardes", "wb") as fichier:
						mon_pickler = pickle.Pickler(fichier)
						tableau_des_scores[nom_du_joueur] = score_du_joueur
						tableau_des_scores = mon_pickler.dump(tableau_des_scores)
						print(
							"You beat your old score! \nYou had", 
							ancien_score, "point(s) and now you have",
							 score_du_joueur, "point(s).\nScore saved."
							 )
				elif ancien_score == score_du_joueur:
					print(
						"You have matched your old score! \nYou have",
						score_du_joueur, "point(s)."
						)
				else:
					print(
						"Your best score is :", 
						ancien_score
						)
def message_accueil():
	phrase_1 = "X means : good color but BAD place.\n"
	phrase_2 = "V means : good color and GOOD place.\n"	
	phrase_3 = "You have 12 tries.\n"	
	return phrase_1 + phrase_2 + phrase_3

def choix_difficulte():
	phrase_1 = "\nHit H to play in Hard level (code may have duplicates).\n"
	phrase_2 = "Hit N to play Normal level"
	print(phrase_1 + phrase_2)
	choix = input("Enter your choice : ")
	choix = choix.capitalize()
	if choix == "H":
		return "hard"
	elif choix == "N":
		return "normal"
	else :
		print("Sorry I did not understand. Please try again.")
		choix_difficulte()		

def sortir(nom):
	phrase_1 = "\n\nTo quit hit Q.\n"
	phrase_2 = "To change player hit P.\n"
	phrase_3 = "To continue hit C.\n"
	print(phrase_1 + phrase_2 + phrase_3)
	saisie = input("Enter your choice. (One letter at a time) : ")
	saisie = saisie.capitalize()

	if saisie == "Q":
		return True, nom	
	elif saisie == "P":
		nom = input("What's your name ? ")
		ouvrir_la_sauvegarde(nom)
		return False, nom
	elif saisie == "C":
		return False, nom
	else:
		print("Sorry I did not understand. Please try again.")
		sortir(nom)

"""
User input management functions------------------------------------------
"""
def verifier_saisie():
	""" 
	The player must enter 4 letters.
	These letters are stored in the authorized list.
	The entry is converted capitals.
	If the entry is not suitable, because there are too many characters
	or that they are not alpha characters, the function
	start over at the beginning.
	Each letter of the entry is stored in the list
	combination.
	If the entry is not suitable, because the letters are not
	not in the authorized list, the function starts again at
	beginning.
	If the entry is suitable, it is returned to the
	main function.

	"""
	autorisee = ["A", "B", "C", "D", "E", "F", "H", "I"]
	combinaison = ["", "", "", ""]
	saisie = input(
		"Choose your combination from these letters : A B C D E F H I :"
		)
	if len(saisie) != 4 or not saisie.isalpha():
		print(
			"Your combination must contain 4 characters among those proposed."
			)
		return verifier_saisie()
	else :
		saisie = (saisie).upper()
		for i, element in enumerate(saisie):
			combinaison[i] = saisie[i]
			for j, lettre in enumerate(saisie):
				if saisie[j] not in autorisee:
					print(
						saisie[j], "is not allowed."
						 )
					return verifier_saisie()
	return combinaison
	
"""
Functions of the secret code---------------------------------------------------
"""

def generer_code_sans_doubles():
	""" 
	The code is a list of "x".
	Each x takes a value between 0 and 7.
	If there is a double, the function starts again from the beginning.
	When the code contains only numbers,
	Each number is converted into a letter among those
	authorized.
	Returns the code in the main function.
	"""
	code = ["x", "x", "x", "x"]
	for i, element in enumerate(code):
		n = str(randrange(8))
		if n in code:
			return generer_code_sans_doubles()
		else :
			code[i] = n
	for j, contenu in enumerate(code):
		if contenu == "0":
			code[j] = "A"
		elif contenu == "1":
			code[j] = "B"
		elif contenu == "2":
			code[j] = "C"
		elif contenu == "3":
			code[j] = "D"
		elif contenu == "4":
			code[j] = "E"
		elif contenu == "5":
			code[j] = "F"
		elif contenu == "6":
			code[j] = "H"
		else:
			code[j] = "I"
	return code

def generer_code():
	""" 
	The code is a list of "x".
	Each x takes a value between 0 and 7.
	Each number is converted into a letter among those
	authorized.
	Returns the code in the main function.
	"""
	code = ["x", "x", "x", "x"]
	for i, element in enumerate(code):
		n = str(randrange(8))
		code[i] = n
	for j, contenu in enumerate(code):
		if contenu == "0":
			code[j] = "A"
		elif contenu == "1":
			code[j] = "B"
		elif contenu == "2":
			code[j] = "C"
		elif contenu == "3":
			code[j] = "D"
		elif contenu == "4":
			code[j] = "E"
		elif contenu == "5":
			code[j] = "F"
		elif contenu == "6":
			code[j] = "H"
		else:
			code[j] = "I"
	return code

def comparaison_couleurs(combinaison, code, compteur_d_essais):
	""" 
	Function which compares the code and the combination of the player
	by looking for color matches.
	- save the combination;
	For each letter in combination :
		if the combination letter has more occurrences than the same 
		letter in the code:
			- Replace excess occurrences in combination with an "x";
	- compare the new combination with the code;
	- increments the test counter by 1
	- returns in the main function:
	- the number of good colors;
	- the test counter;
	- saving the combination.

	"""
	bonnes_couleurs = 0
	sauvegarde_combinaison = []
	sauvegarde_combinaison.extend(combinaison)
	for i, element in enumerate(combinaison):
		for j, letter in enumerate(code):				
			if combinaison.count(element) > code.count(letter):
				if element == letter:					
					del combinaison[i]
					combinaison.insert(i, "x")					
		if combinaison[i] in code:
			bonnes_couleurs += 1
	compteur_d_essais += 1
	return bonnes_couleurs, compteur_d_essais, sauvegarde_combinaison

def comparaison_places(combinaison, code):
	"""
	Function that searches for well-placed colors:
	Compares the colors for each similar index of the
	combination list and code list.
	Returns the number of well-placed colors. 
	"""
	bonnes_places = 0
	for i, element in enumerate(combinaison):
		for j, letter in enumerate(code):
			if i == j:
				if element == letter:
					bonnes_places +=1
	return bonnes_places
