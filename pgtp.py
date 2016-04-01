import sys

class PGTP:
	def __init__(self):
		self.barCount = 0
		self.gameTypeList = ["unused", "Petersen Graph", "Complete Graph", "Hypercube Graph"]
		self.gameFormatList = ["unused", "Random Game", "Logical Game"]
		while True:
			self.printIntro()
			gameType = self.getGameType()
			gameFormat = self.getGameFormat()
			numNodes = self.getNumNodes(gameType)
			numDims = self.getNumDims(gameType)
			edgeWeight = self.getEdgeWeight()
			numGames = self.getNumGames()
			viewGames = self.getViewGames()
			self.parseChoice(gameType, gameFormat, numNodes, numDims, edgeWeight, numGames, viewGames)

	def printIntro(self):
		print("Welcome to the Text-Based Graph Theory Logging Program")

	def getGameType(self):
		print("\nWhat type of graph would you like to use?")
		print("1. Petersen Graph")
		print("2. Complete Graph")
		print("3. Hypercube Graph")
		print("9. Quit program")
		choice = int(input("Please enter your choice: "))
		# Check right away for 9
		if choice == 9:
			print("Exiting program.")
			sys.exit(0)
		return choice

	def getGameFormat(self):
		print("\nWhat game format would you like to use?")
		print("1. Random Game")
		print("2. Logical Game")
		return int(input("Please enter your choice: "))

	def getNumNodes(self, gameType):
		if gameType == 2:
			print("\nHow many nodes would you like in this graph?")
			return int(input("Please enter your choice (>1): "))
		else:
			return -1
	
	def getNumDims(self, gameType):
		if gameType == 3:
			print("\nHow many dimensions would you like?")
			print("\tCurrently limited to 2-4")
			return int(input("Please enter your choice (2-4): "))
		else:
			return -1

	def getEdgeWeight(self):
		print("\nWhat weight would you like to assign to the edges?")
		print("\tNote: Type '0' for a random weight for each edge, between 1 and 10")
		return int(input("Please enter your choice: "))

	def getNumGames(self):
		print("\nHow many games would you like to simulate?")
		return int(input("Please enter your choice: "))

	def getViewGames(self):
		print("\nWould you like to view the games as they are beign played?")
		print("\tNote: If you are running more than 10 million games, or")
		print("\tif you want a cleaner terminal, 'n' recommended.")
		return str(input("Please enter your choice (y/n): "))

	def parseChoice(self, gameType, gameFormat, numNodes, numDims, edgeWeight, numGames, viewGames):
		print("\n\nHere are your choices:")
		print("Game type: %s" % self.gameTypeList[gameType])
		print("Game format: %s" % self.gameFormatList[gameFormat])
		if numNodes != -1:
			print("Number of nodes: %d" % numNodes)
		if numDims != -1:
			print("Number of dimensions: %d" % numDims)
		if edgeWeight == 0:
			print("Edge weight: Random")
		else:
			print("Edge Weight: %d" % edgeWeight)
		print("Number of games: %d" % numGames)
		if viewGames.lower() == 'y':
			print("View Games: True")
		else:
			print("View Games: False")
		print("\nDoes this look correct?")
		print("'y' to continue, 'n' to start over")
		choice = str(input("Please enter your choice (y/n): "))
		if choice.lower() == 'n':
			return
		else:
			print("Working!")
			sys.exit(0)

# Start the program
x = PGTP()
