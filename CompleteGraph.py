import Node.py
import random

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

