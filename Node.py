class Node:
	def __init__(self, n):
		self.name = n
		self.nodelist = {}
		setDegree()

	def getName(self):
		return name

	def printEdges(self):
		print("Node", self.name, "is connected to the following nodes: ")
		if len(self.nodeList) == 0:
			print("This node is not connected to any other node.")
		else:
			for node, weight in self.nodeList.items():
				print("N", node, "-", weight, "- N", node.getName())
		print()

	def getEdgeListSize(self):
		return len(self.nodeList)

	def getMinimalDegreeNode(self):
		for node, weight in self.nodeList.items():
			node.setDegree()
		minimalDegreeNode = self.nodeList[0]
		for node, weight in self.nodeList.items():
			if node.getDegree() < minimalDegreeNode.getDegree():
				minimalDegreeNode = node
		return node.
		