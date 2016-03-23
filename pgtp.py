import sys

class PGTP:
	def __init__(self):
		self.barCount = 0
		self.printIntro()
		choice = self.printStartMenu()
		parseChoice(choice)

	def printIntro(self):
		print("Welcome to the Text-Based Graph Theory Logging Program\n")

	def printStartMenu(self):
		print("What type of graph would you like to use?")
		print("1. Petersen Graph")
		print("2. Complete Graph")
		print("3. Hypercube Graph")
		print("9. Quit program")
		return int(input("Please enter your choice: "))

	def parseChoice(self, choice):
		


if "__name__" == "__main__":
	x = PGTP()

