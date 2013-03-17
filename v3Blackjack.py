#Blackjack - Third Try! 
import random

#  .o88b. db       .d8b.  .d8888. .d8888. d88888b .d8888.
# d8P  Y8 88      d8' `8b 88'  YP 88'  YP 88'     88'  YP
# 8P      88      88ooo88 `8bo.   `8bo.   88ooooo `8bo.  
# 8b      88      88~~~88   `Y8b.   `Y8b. 88~~~~~   `Y8b.
# Y8b  d8 88booo. 88   88 db   8D db   8D 88.     db   8D
#  `Y88P' Y88888P YP   YP `8888Y' `8888Y' Y88888P `8888Y'

class Game:
	def __init__(self):
		self.name = "Blackjack"
	def createDealer():
		dealer = Player("Dealer", 0)
	def createPlayer():
		wallet = raw_input("How much money you got? 1-1000: ")
		player = Player("Player", wallet)
	def placeBets():
		bet = raw_input("Place your bet! ")
	def initialDeal(player):
		deal(player.hand)
		deal(player.hand)
		player.hand.printHand()
		print "Value: " + str(player.hand.value)
	def printMe():
		

class Player:
	def __init__(self, name, wallet):          #for now, name must be "Player" or "Dealer"
		self.name = name
		self.hand = Hand(self.name)
		self.wallet = wallet
	def printStats(self):
		print self.name + " has $" + str(self.wallet)

class Card:
	def __init__(self, suite, number):
		self.family = suite
		if number == 11:
			self.rank = "Jack"
		elif number == 12:
			self.rank = "Queen"
		elif number == 13:
			self.rank = "King"
		elif number == 1:
			self.rank = "Ace"
		else:
			self.rank = str(number)
		if number < 10:
			self.value = number
		elif number >=10:
			self.value = 10
	def printCard(self):
		print str(self.rank), self.family

class Deck():
	def __init__(self):
		self.cardList = []
		self.size = 52
		for s in [u"\u2665", u"\u2663", u"\u2660", u"\u2666"]:	#Suite Order: Hearts, Clubs, Spades, Diamonds
			for n in range(1, 14):
				self.cardList.append(Card(s, n))
	def printDeck(self):
		for card in self.cardList:
			card.printCard()
	def adjustDeck(self):
		self.size = len(self.cardList)

class Hand():
	def __init__(self, name):
		self.hand = []
		self.value = 0 
		self.name = name
		self.hasAce = False
		self.hasJack = False
	def addCard(self, card):
		self.hand.append(card)
		self.value = 0
		if card.rank == "Jack":
			self.hasJack = True
		elif card.rank == "Ace":
			self.hasAce = True
		for i in self.hand:
			self.value = self.value + i.value
		if self.hasAce == True:
			if self.value <= 11:
				self.value = self.value + 10
	def printHand(self):
		hand = []
		for i in range(len(self.hand)):
			self.hand[i].printCard()

createPlayer()