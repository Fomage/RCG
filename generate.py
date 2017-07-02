import random
import ColiseeMain
import re
random.seed()

############# Parameters #############

characterBank="characters.csv"

############# Functions #############

def parseMainFile(mainFilePath):
	with open(mainFilePath, "r") as f:
		lines = f.readlines()
		res = {}
		tags = {}
		currentTag = None
		for l in lines:
			if re.search(r"#-+[a-zA-Z ]+-+", l):
				currentTag = re.search(r"#-+(?P<tagName>[a-zA-Z ]+)-+",l).group("tagName")
				print(currentTag)
				tags[currentTag] = ""
			else:
				if currentTag:
					tags[currentTag] += l
		return tags

def csvToPython(characterBankPath):
	characters = ColiseeMain.loadCharacters(characterBankPath)
	res = "characterList = []\n"
	for character in characters:
		res += "characterList.append(Character("
		res += '"' + character.name + "\", "
		res += '"' + character.creator + "\", "
		res += '"' + character.source + "\", "
		res += '"' + character.world + "\", "
		res += '"' + str(character.powerLevel) + "\", "
		res += "["
		if character.tags:
			for tag in character.tags:
				res += tag + ","
		res += "]"
		res += "))\n"
	return res

############# Actual build #############

content = ""
blocks = parseMainFile("ColiseeMain.py")

# imports
content += "import random\n"

# class definitions
content += blocks["Class definitions"]

# utility function
content += blocks["FUNCTIONS"]

# load characters
content += csvToPython(characterBank)

# play module
content += blocks["Play Module"]

############## output ###############
with open("RCG.py", "w") as f:
	f.write(content)
# f = open('RCG.py','w')
# with open('RCG.py','w') as f:
# 	f.write("\nimport random\nrandom.seed()\n\nsource={}\nkeys=[]\n\n")
# 	for key in source:
# 		f.write('#'+key+'\nkeys+=["'+key+'"]\nsource["'+key+'"]=[]\n')
# 		for value in source[key]:
# 			f.write('source["'+key+'"]+=["'+value+'"]\n')

# 	fname="GameObject.py"
# 	with open(fname) as f2:
# 		f.write(f2.read())
