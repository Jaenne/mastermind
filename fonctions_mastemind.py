#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

"""
Toutes les fonctions du Mastermind.
"""

import os
import pickle
from random import randrange
from package.donnees import *
os.chdir(".")
"""
Fonctions de menu --------------------------------------------------------------------
"""
def ouvrir_le_fichier_sauvegardes():
	"""
	Cette fonction vérifie que le fichier "sauvegardes" existe
	si oui, elle renvoie le contenu dans la fonction main.
	si non, elle créer le fichier "sauvegarde" avec un tableau des scores vide.
		puis elle renvoie le contenu dans la fonction main.
	"""
	if os.path.exists(fichier_de_sauvegardes):
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
	Cette fonction ouvre le fichier "sauvegardes"
	puis vérifie que le joueur a une sauvegarde à son nom.
	si oui, elle renvoie le score du joueur dans la fonction main.
	si non, elle créer une sauvegarde au nom du joueur avec 0 point.
		puis renvoie le score du joueur dans la fonction main.
	"""
	with open("sauvegardes", "rb") as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		tableau_des_scores = mon_depickler.load()
		for k, v in tableau_des_scores.items():
			if k == nom_du_joueur:
				score_du_joueur = v
				return score_du_joueur
	with open("sauvegardes", "wb") as fichier:
		mon_pickler = pickle.Pickler(fichier)
		score_du_joueur = 0
		tableau_des_scores[nom_du_joueur] = score_du_joueur
		tableau_des_scores = mon_pickler.dump(tableau_des_scores)
		return score_du_joueur

def enregistrer_le_score(nom_du_joueur, score_du_joueur):
	"""
	La fonction vérifie si le score du joueur est supérieur à son ancien meilleur 
	score.
	Si oui, elle écrase l'ancien score et enregistre le nouveau meilleur score.
	si non, elle ne touche pas au fichier de sauvegarde.
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
							"Vous avez battu votre ancien score ! \nVous aviez", 
							ancien_score, "point(s) et maintenant vous avez",
							 score_du_joueur, "point(s).\nScore sauvegardé."
							 )
				elif ancien_score == score_du_joueur:
					print(
						"Vous avez égallé votre ancien score ! \nVous avez",
						score_du_joueur, "point(s)."
						)
				else:
					print(
						"Votre meilleur score est :", 
						ancien_score
						)

def sortir():
	quitter = input("Pour quitter taper Q:")
	if quitter == "q" or quitter == "Q" :
		return True
	else:
		return False

"""
Fonctions de gestion des saisies utilisateur------------------------------------------
"""
def verifier_saisie():
	""" La saisie du joueur doit comporter 4 Lettres.
	Ces lettres sont stockées dans la liste autorisée.
	La saisie est convertie capitales.
	Si la saisie ne convient pas, car il y trop de caracteres
	ou qu'il ne s'agit pas de caractères alpha, la fonction
	recommence au début.
	Chaque lettre de la saisie est stockée dans la liste
	combinaison.
	Si la saisie ne convient pas, car les lettres ne sont
	pas dans la liste autorisée, la fonction recommence au
	début.
	Si la saisie convient, elle est renvoyée dans la
	fonction main.
	"""
	autorisee = ["A", "B", "C", "D", "E", "F", "H", "I"]
	combinaison = ["", "", "", ""]
	saisie = input(
		"Choisissez votre combinaison parmi ces lettres : A B C D E F H I :"
		)
	if len(saisie) != 4 or not saisie.isalpha():
		print(
			"Votre combinaison doit comporter 4 caractères parmi ceux proposés."
			)
		return verifier_saisie()
	else :
		saisie = (saisie).upper()
		for i, element in enumerate(saisie):
			combinaison[i] = saisie[i]
			for j, lettre in enumerate(saisie):
				if saisie[j] not in autorisee:
					print(
						saisie[j], "n'est pas autorisée."
						 )
					return verifier_saisie()
	return combinaison
	
"""
Fonctions du corps du jeu ------------------------------------------------------------
"""

def generer_code_sans_doubles():
	""" Le code est une liste de "x".
	Chaque x prend une valeur ente 0 et 7.
	S'il y a un double, la fonction recommence au début.
	Lorsque le code ne contient que des chiffres,
	Chaque chiffre est convertit en lettre parmi celles
	autorisées.
	Renvoie le code dans la fonction main.
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

def comparaison_couleurs(combinaison, code, compteur_d_essais):
	""" Fonction qui compare le code et la combinaison du joueur
	en cherchant les correspondances de couleur.
	- sauvegarde la combinaison ;
	- Remplace les doubles par un "x" ;
	- compare la combinaison sans doubles avec le code ;
	- incrémente de 1 le compteur d'essais 
	- renvoie dans la fonction main :
		- le nombre de bonnes couleurs ;
		- le compteur d'essais ;
		- la sauvegarde de la combinaison.
	"""
	bonnes_couleurs = 0
	sauvegarde_combinaison = []
	sauvegarde_combinaison.extend(combinaison)
	for i, element in enumerate(combinaison):
		if combinaison.count(element) > 1:
			del combinaison[i]
			combinaison.insert(i, "x")
		if combinaison[i] in code:
			bonnes_couleurs += 1
	compteur_d_essais += 1
	return bonnes_couleurs, compteur_d_essais, sauvegarde_combinaison

def comparaison_places(tableau_combinaison, tableau_code):
	""" Fonction qui cherche les couleurs bien placées: 
	Compare les couleurs pour chaque index similaires du
	tableau combinaison et du tableau code.
	Retourne le nombre de couleurs bien placées. """
	bonnes_places = 0
	for k, v in tableau_combinaison.items():
		for key, value in tableau_code.items():
			if k == key:
				if v == value:
					bonnes_places +=1
	return bonnes_places

def transformer_en_tableau(liste):
	tableau_liste = {}
	for i, lettre in enumerate(liste):
		tableau_liste[i] = lettre
	return tableau_liste

def afficher_tableau(tableau, texte):
	for k, v in tableau.items():
		print(texte, ": {} : {}".format(k,v))
