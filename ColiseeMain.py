# -*-coding:Latin-1 -*

import os
#currentDirectory = os.path.dirname(__file__)
#os.chdir("C:/Users/Zen/Documents/Progra/Python/Colisee")

import random


#-------Class definitions--------

class Character:
	"""Character's attributes:
	- ID: unique integer
	- name: string
	- creator: string
	- source: string, the book/movie/other work from which the character is extracted
	- world: string
	- powerLevel: integer
	- tags: array[string]
	- alreadyPicked: boolean
	"""
	currentCharacterId = 0

	def __init__(self, ID, name, creator, source, world, powerLevel, tags):
		"""default empty initialization"""
		Character.currentCharacterId +=1

		self.ID = ID
		self.name = name
		self.creator = creator
		self.source = source
		self.world = world
		self.powerLevel = powerLevel
		self.tags = tags

		self.alreadyPicked = False

	def hasBeenPicked(self):
		return self.alreadyPicked

	def pick(self):
		self.alreadyPicked = True

class Player:
	"""Player's attributes:
	- ID: unique integer
	- character: Character
	"""
	currentPlayerId = 0
	defaultCharacterSublist = []
	def __init__(self, characterSublist = None, **options):
		self.ID = Player.currentPlayerId
		Player.currentPlayerId +=1

		if(characterSublist == None):
			characterSublist = self.defaultCharacterSublist

		self.character = random.choice([character for character in characterSublist if not character.hasBeenPicked()])
		self.character.pick()

		print ("Player {} : {}".format(self.ID, self.character.name))

	def repick(self, persoSubList = None):
		if persoSubList == None:
			persoSubList = Player.defaultCharacterSublist

		self.character = random.choice([perso for perso in persoSubList if not perso.hasBeenPicked()])
		self.character.pick()

		print ("Player {}'s character changed to {}.\n".format(self.ID, self.character.name))

	def __str__(self):
		return "Player {} : {}".format(self.ID, self.character.name)

#--------INIT--------------
characterList = []
# Load every Characters :

charactersFile = open("characters.csv", "r")
content = charactersFile.read()
content = content.replace(";;", ";")
content = content.replace(";\n", "\n")
content = content.split("\n")
content = [line.split(";") for line in content[1:-1]]
for line in content:
	if line[-1] == '':
		del line[-1]
# Rebuild tag list
for i, line in enumerate(content):
	tags = line[6:]
	content[i] = line[:6] + [tags]
for line in content:
	characterList.append(Character(*line))

charactersFile.close()

# Character selection by tag

def restrictCharacterListByTag(characterListToRestrict, tag):
	result = []
	for character in characterListToRestrict:
		if tag in character.tags:
			result.append(character)
	return result

def restrictCharacterListByTags(characterListToRestrict, tags):
	for tag in tags:
		characterListToRestrict = restrictCharacterListByTag(characterListToRestrict, tag)
	return characterListToRestrict
	
#-------TESTS-------------

#Test restrictCharacterListByTag
'''
testList = restrictCharacterListByTag(characterList, "Fantasy")
i = 0
for perso in testList :
	i+=1
	print (perso.name + "\n")
	for tag in perso.tags :
		print ("\t" + tag + "\n")
print (i)
'''
'''
#Test restrictListWithTags
testList = restrictCharacterListByTags(characterList, ["Fantasy", "Badass"])
i = 0
for perso in testList :
	i+=1
	print (perso.name + "\n")
	for tag in perso.tags :
		print ("\t" + tag + "\n")
print (i)
'''

#-------Mode Selector----
# Quid de mettre un dictionnaire qui renvoie des procedures en sortie, procedures qui lancent le type de partie selectionnee ?
'''
def modesEnum(modeName):
	return {
	'': ,}
'''

#-------Play Module-------
gameMode = input("Choose gamemode:\n0:default\n1:tagged\n2:world\n3:power")

nbPlayers = int(input("How many Players?"))

Player.defaultCharacterSublist = characterList
Players = []
for i in range(0, nbPlayers):
	Players.append(Player(characterList))

repickAnswer = input("Repick ? ")
while str(repickAnswer) != "no":
	Players[int(repickAnswer)].repick()
	for p in Players :
		print(p)
	repickAnswer = input("Repick ? ")




