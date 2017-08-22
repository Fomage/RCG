#------Imports------
import os
#currentDirectory = os.path.dirname(__file__)
#os.chdir("C:/Users/Zen/Documents/Progra/Python/Colisee")

import random

import csv


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

  def __init__(self, name, creator, source, world, powerLevel, tags):
    """default empty initialization"""
    Character.currentCharacterId +=1

    self.ID = Character.currentCharacterId
    self.name = name
    self.creator = creator
    self.source = source
    self.world = world
    self.powerLevel = powerLevel
    self.tags = tags

    self.alreadyPicked = False

  def hasBeenPicked(self):
    return self.alreadyPicked

  def pick(self, b = True):
    self.alreadyPicked = b

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

    print(self)

  def repick(self, persoSubList = None):
    if persoSubList == None:
      persoSubList = Player.defaultCharacterSublist

    self.character = random.choice([perso for perso in persoSubList if not perso.hasBeenPicked()])
    self.character.pick()

    print ("Player {}'s character changed to {}.".format(self.ID, self.character.name))

  def __str__(self):
    res = "Player {} : {} ({})".format(self.ID, self.character.name, self.character.source)
    if not res:
      print(self.character)
    return res

#--------Characters Loading--------------
def loadCharacters(filePath):
  with open("characters.csv") as charactersCsvFile:
    res = []
    characterReader = csv.reader(charactersCsvFile)
    firstRow = True
    for row in characterReader:
      if firstRow:
        firstRow = False
      else:
        if(len(row) > 5):
          row[5] = row[5:]
        else:
          while len(row) <= 5:
            row.append(None)
        res.append(Character(*row))
    return res

#--------FUNCTIONS--------------

# Reset character list

def resetCharacterList(characterList):
  for character in characterList:
    character.pick(False)

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

#-------PrePlay Module---------

# load characters
if __name__ == "__main__":
  characterList = loadCharacters("characters.csv")

#-------Play Module-------
if __name__ == "__main__":
  # input constants
  no = "no"

  # gameMode = input("Choose gamemode:\n0:default\n1:tagged\n2:world\n3:power")

  # Character list selection
  Player.defaultCharacterSublist = characterList

  while True:
    # character list reset
    resetCharacterList(characterList)

    # Player number selection
    nbPlayers = int(input("How many Players?"))
    players = []
    Player.currentPlayerId = 0
    for i in range(0, nbPlayers):
      players.append(Player(characterList))

    # Repicks
    answer = input("Repick/swap ? ")
    while answer != no:
      arrayAnswer = answer.split()
      if len(arrayAnswer) == 2:# swap
        arrayAnswer[0] = int(arrayAnswer[0]) % len(players)
        arrayAnswer[1] = int(arrayAnswer[1]) % len(players)
        temp = players[arrayAnswer[0]].character
        players[arrayAnswer[0]].character = players[arrayAnswer[1]].character
        players[arrayAnswer[1]].character = temp
      elif len(arrayAnswer) == 1:# repick
        if int(answer) < 0: # repick all
          resetCharacterList(characterList)
          for p in players:
            p.repick()
        else: # repick one
          answer = int(answer) % len(players)
          players[answer].repick()
      else:
        print("Unkown instruction ignored.")
      for p in players:
        print(p)
      answer = input("Repick ? ")




