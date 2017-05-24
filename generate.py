import random
random.seed()

############# Parameters #############

fname="CharactersBank.txt"

############# Initialization #############

source = {}
lines=[]
currentKey=""
keys=[]

with open(fname) as f:
	lines = f.readlines()

for l in lines:
	if l[0]=='\t':
		source[currentKey]+=[l[1:-1]]
	elif l[0]=='\n':
		currentKey=""
	else:
		currentKey=l[:-1]
		keys+=[currentKey]
		source[currentKey]=[]

print("Number of sources : "+str(len(source)))

#output
f = open('RCG.py','w')
f.write("\nimport random\nrandom.seed()\n\nsource={}\nkeys=[]\n\n")
for key in source:
	f.write('#'+key+'\nkeys+=["'+key+'"]\nsource["'+key+'"]=[]\n')
	for value in source[key]:
		f.write('source["'+key+'"]+=["'+value+'"]\n')

fname="GameObject.py"
with open(fname) as f2:
	f.write(f2.read())

f.close()
############# Functions #############


