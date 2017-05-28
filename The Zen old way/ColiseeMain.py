# -*-coding:Latin-1 -*

import os
#currentDirectory = os.path.dirname(__file__)
#os.chdir("C:/Users/Zen/Documents/Progra/Python/Colisee")

import random


#-------Class definitions--------

class Personnage:
	"""Un personnage est caractérisé par :
	- son ID : un entier unique
	- son nom : une chaîne
	- son créateur
	- son oeuvre
	- son univers
	- son facteur de puissance
	- des tags
	- un booleen, alreadyPicked, qui indique si le personnage a déjà été tiré auparavant
	"""
	personnagesCrees = 0
	
	def __init__(self, ID, nom, createur, oeuvre, univers, facteurDePuissance, tags):
		"""default empty initialization"""
		Personnage.personnagesCrees +=1
		
		self.ID = ID
		self.nom = nom
		self.createur = createur
		self.oeuvre = oeuvre
		self.univers = univers
		self.facteurDePuissance = facteurDePuissance
		self.tags = tags
		
		self.alreadyPicked = False
		
	def hasBeenPicked(self):
		return self.alreadyPicked
	
	
	def pick(self):
		self.alreadyPicked = True

	
		


class Joueur:
	"""Un joueur possède :
	- un IDj
	- un personnage
	"""
	currentIDj = 0
	persoDefaultSubList = []
	def __init__(self, persoSubList, **options):
		self.IDj = Joueur.currentIDj
		
		if Joueur.currentIDj == 0:
			Joueur.persoDefaultSubList = persoSubList #On met à jour la liste de personnages par défaut
		
		Joueur.currentIDj +=1
		
		self.personnage = random.choice([perso for perso in persoSubList if not perso.hasBeenPicked()])
		self.personnage.pick()
		


		print ("Joueur {} : {}".format(self.IDj, self.personnage.nom))
		
	def repick(self, persoSubList = []):
		if persoSubList == []:
			persoSubList = Joueur.persoDefaultSubList
		
		self.personnage = random.choice([perso for perso in persoSubList if not perso.hasBeenPicked()])
		self.personnage.pick()
		
		print ("Joueur {} a chang� de personnage. Il a maintenant {}.\n".format(self.IDj, self.personnage.nom))
		

#--------INIT--------------
persoList = []
# On charge tous les personnages :


fichierPersonnages = open("personnages.csv", "r")
contenu = fichierPersonnages.read()
contenu = contenu.replace(";;", ";")
contenu = contenu.replace(";\n", "\n")
contenu = contenu.split("\n")
contenu = [ligne.split(";") for ligne in contenu[1:-1]]
for ligne in contenu:
        if ligne[-1] == '':
                del ligne[-1]
# On reconstitue la liste des tags
for i, ligne in enumerate(contenu):
        tags = ligne[6:]
        contenu[i] = ligne[:6] + [tags]
for ligne in contenu:
	persoList = persoList + [Personnage(*ligne)]


fichierPersonnages.close()

#Sélection par tags

def restrictPersoListSingleTag(persoListToRestrict, tag):
	result = []
	for perso in persoListToRestrict:
		if tag in perso.tags:
			result = result + [perso]
	return result

def restrictPersoListWithTags(persoListToRestrict, tags):
	for tag in tags:
		persoListToRestrict = restrictPersoListSingleTag(persoListToRestrict, tag)
	return persoListToRestrict
	
#-------TESTS-------------

#Test restrictPersoListSingleTag
'''
testList = restrictPersoListSingleTag(persoList, "Fantasy")
i = 0
for perso in testList :
	i+=1
	print (perso.nom + "\n")
	for tag in perso.tags :
		print ("\t" + tag + "\n")
print (i)
'''
'''
#Test restrictListWithTags
testList = restrictPersoListWithTags(persoList, ["Fantasy", "Badass"])
i = 0
for perso in testList :
	i+=1
	print (perso.nom + "\n")
	for tag in perso.tags :
		print ("\t" + tag + "\n")
print (i)
'''

#-------Mode Selector----
'''Quid de mettre un dictionnaire qui renvoie des procédures en sortie, procédures qui lancent le type de partie sélectionnée ?'''
'''
def modesEnum(modeName):
	return {
	'': ,}
'''
	
#-------Play Module-------
gameMode = input("Choisissez un mode de jeu : default, tagged, universe, power")

nbJoueurs = int(input("Combien de joueurs : "))
joueurs = []

for i in range(0, nbJoueurs):
	joueurs = joueurs + [Joueur(persoList)]

print("\nRepick ? ")
repickAnswer = input()
while repickAnswer != "no":
        joueurs[int(repickAnswer)].repick()
        for j in joueurs :
                print("Joueur {} : {} ".format(j.IDj, j.personnage.nom))
        print("\nRepick ? ")
        repickAnswer = input()
        
		



