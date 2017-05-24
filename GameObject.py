

class Game(object):
	roles=[]
	usedSources=[]
	n=0
	ds=True#different sources

	def __init__(self, n,differentSource=True):
		self.n=n
		self.df=differentSource
		for i in range(n):
			self.roles.append(["",""])
		for i in range(len(source)):
			self.usedSources.append(False)
		self.roll(-1)

	def printAll(self):
		for i in range(self.n):
			print(str(i)+" : "+self.roles[i][1]+" ("+self.roles[i][0]+")")
	
	def roll(self, index=-1):
		if(index < 0):
			if self.df:
				sum=0
				for i in range(len(source)):
					if self.usedSources[i]:
						sum+=1
				if(len(source)-sum<self.n):
					print("Sources reset")
					for i in range(len(source)):
						self.usedSources[i]=False
				for i in range(self.n):
					r=random.randint(0,len(source)-1-i)
					j=0
					k=0
					while(k<r):
						j+=1
						if not self.usedSources[j]:
							k+=1
					self.usedSources[j]=True
					self.roles[i][0]=keys[j]
					r=random.randint(0,len(source[keys[j]])-1)
					self.roles[i][1]=source[keys[j]][r]
			else:
				for i in range(self.n):
					goon=True
					while goon:
						goon=False
						r=random.randint(0,len(source)-1)
						self.usedSources[r]=True
						self.roles[i][0]=keys[r]
						p=random.randint(0,len(source[keys[r]])-1)
						self.roles[i][1]=source[keys[r]][p]
						for j in range(i):
							goon = goon or (self.roles[j][0]==self.roles[i][0] and self.roles[j][1]==self.roles[i][1])
		else:
			if self.df:
				oldSource=self.roles[index][0]
				r=random.randint(0,len(source)-1-self.n)
				j=0
				k=0
				while(k<r):
					j+=1
					if not self.usedSources[j]:
						k+=1
				self.usedSources[j]=True
				self.roles[index][0]=keys[j]
				r=random.randint(0,len(source[keys[j]])-1)
				self.roles[index][1]=source[keys[j]][r]
				for i in range(len(source)):
					bol=False
					for role in self.roles:
						bol = bol or role[0]==keys[i]
					self.usedSources[i]=bol
			else:
				goon=True
				while goon:
					goon=False
					r=random.randint(0,len(source)-1)
					if self.roles[index][0]!=keys[r]:
						self.roles[index][0]=keys[r]
						p=random.randint(0,len(source[keys[r]])-1)
						self.roles[index][1]=source[keys[r]][p]
						for j in range(self.n):
							goon = goon or (self.roles[j][0]==self.roles[index][0] and self.roles[j][1]==self.roles[index][1] and j!=index)
					else:
						goon=True
		self.printAll()


diffSources=int(input("Use different sources ?\n"))
n=int(input("How many characters must be generated ?\n"))
g=None
if(diffSources==0):
	g=Game(n,False)
else:
	g=Game(n,True)
while True:
	i=int(input("Reroll someone ?\n"))
	g.roll(i)

