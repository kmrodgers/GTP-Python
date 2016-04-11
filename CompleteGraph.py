import Node.py
import Token.py
import random

MASTER_DATA_PATH = "output_data/master_data.txt"

class CompleteGraph:
	def __init__(self, gameFormat, numNodes, edgeWeight, numGames, viewGames):
		self.nodeList = []
		self.numGames = numGames
		self.viewGames = viewGames
		self.createNodes(numNodes)
		self.createEdges(edgeWeight, gameFormat)
		#C'mon, play the game, everybody play the gaaaaaaaaaame!
		self.playTheGame()

	def createNodes(self, numNodes):
		for i in range(1, numNodes+1):
			n = Node(i)
			nodeList.append(n)

	def createEdges(self, edgeWeight):
		for i in nodeList:
			for j in nodeList:
				if (i != j):
					if self.gameFormat == 1:
						randValue = getRandomNumber(10)
						i.setEdge(j, randValue)
						j.setEdge(i, randValue)
					else:
						i.setEdge(j, edgeWeight)
						j.setEdge(i, edgeWeight)

	def getRandomNumber(self, size):
		return random.randint(1, size)

	def getRandomEdge(self, size):
		return random.randint(1, size) + 1;

	def playTheGame(self):
		# Open the file
		masterData = open(MASTER_DATA_PATH, "w")
		# Setup the token with the first Node
		t = Token(nodeList[0])
		# Variables for random stuff...
		netRandomWeight = 0
		edgeSize = 0
		nextMove = 0
		# If we are watching the game
		if watch:
			# Write to file
			master_data.write(t.getTokenLocation().getName(), "-")
			# Play the game
			while (true):
				# If it's player 2's turn
				if t.getCurrentPlayerTurn() == 2:
					netMove = getRandomNumber(t.getTokenLocation().getEdgeListSize())
					nextMoveNode = t.getTokenLocation().getNodeAtElement(nextMove)
					edgeSize = t.getTokenLocation().getWeight(nextMoveNode)
					nextRandomWeight = getRandomEdge(edgeSize)
				else:
					nextMoveNode = t.getTokenLocation().getMinimalDegreeNode()
					nextRandomWeight = t.getTokenLocation().getWeight(nextMoveNode)
				if nextRandomWeight > 0:
					master_data.write(nextRandomWeight, "-")
					t.getTokenLocation().removeEdgeWeight(nextMoveNode, nextRandomWeight)
					nextModeNode.removeEdgeWeight(t.getTokenLocation(), nextRandomWeight)
					


			