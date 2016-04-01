import Node.py
import random

class CompleteGraph:
	def __init__(self, gameFormat, numNodes, edgeWeight, numGames, viewGames):
		self.nodeList = []
		self.gameFormat = gameFormat
		self.edgeWeight = edgeWeight
		self.numGames = numGames
		self.viewGames = viewGames
		self.createNodes(numNodes)
		self.createEdges(edgeWeight)
		#C'mon, play the game, everybody play the gaaaaaaaaaame!
		self.playTheGame()

	def createNodes(self, numNodes):
		for i in range(1, numNodes+1):
			n = Node(i)
			nodeList.append(n)

	def createEdges(self, edgeWeight):
		if edgeWeight == 0:

	def getRandomNumber(self, size):
		return random.randint(1, size)