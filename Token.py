import Node.py

class Token:
	def __init__(self, n):
		self.location = n
		self.playerTurn = 1

	def getTokenLocation(self):
		return location

	def setTokenLocation(self, n):
		location = n

	def getPlayerTurn(self):
		return playerTurn

	def setPlayerTurn(self):
		if playerTurn == 1:
			playerTurn = 2
		else:
			playerTurn = 1