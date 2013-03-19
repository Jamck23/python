#Blackjack - Third Try! 

import random
import time

#  .o88b. db       .d8b.  .d8888. .d8888. d88888b .d8888.
# d8P  Y8 88      d8' `8b 88'  YP 88'  YP 88'     88'  YP
# 8P      88      88ooo88 `8bo.   `8bo.   88ooooo `8bo.  
# 8b      88      88~~~88   `Y8b.   `Y8b. 88~~~~~   `Y8b.
# Y8b  d8 88booo. 88   88 db   8D db   8D 88.     db   8D
#  `Y88P' Y88888P YP   YP `8888Y' `8888Y' Y88888P `8888Y'

#Classes: Card, Deck, Hand, Player, Game

class Card:
	def __init__(self, suite, number):
		self.symbols = [u"\u2665", u"\u2663", u"\u2660", u"\u2666"]     #Suite Order: Hearts, Clubs, Spades, Diamonds
		self.names = ["Joker", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
		self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
		
		self.symbol = self.symbols[suite]
		self.name = self.names[number]
		self.value = self.values[number]		

	def printCard(self):
		print self.symbol, self.name, "   ",


class Deck():
	def __init__(self):
		self.cardList = []
		self.size = 52
		for s in range(4):	
			for n in range(1,14):
				self.cardList.append(Card(s, n))

	def printDeck(self):
		for card in self.cardList:
			card.printCard()

	def dealMe(self):
		pick = random.randrange(1, self.size)
		card = self.cardList[pick]
		self.cardList.pop(pick)
		self.size = len(self.cardList)
		return card


class Hand():
	def __init__(self):
		self.cardList = []
		self.value = 0
		self.hasAce = False
		self.hasJack = False

	def addCard(self, card):
		self.cardList.append(card)
		self.value = 0
		if card.name == "Jack":
			self.hasJack = True
		elif card.name == "Ace":
			self.hasAce = True
		for i in self.cardList:
			self.value = self.value + i.value
		if self.hasAce == True:
			if self.value <= 11:
				self.value = self.value + 10

	def printHand(self):
		for card in self.cardList:
			card.printCard()

	def hasBlackjack(self):
		if len(self.cardList) == 2:
			if self.hasAce and self.hasJack:
				return True
			else:
				return False
		else:
			return False

	def handFinished(self):
		if self.value >= 21:
			return True
		else:
			return False


class Player:
	def __init__(self, name, wallet):
		self.name = name
		self.wallet = wallet
		self.bet = 0
		self.hand = Hand()
	def printStats(self):
		print "Welcome " + self.name + "! You have $" + str(self.wallet) + " to gamble away!"
	def printMe(self):
		print self.name
		print self.wallet
		self.hand.printHand()


class Game:
	def __init__(self):
		self.player = Player(raw_input("What is your name? "), input("How much money you got? "))
		self.dealer = Player("Dealer", 0)
		self.deck = Deck()
		self.message = "Welcome to Jampack Blackjack!"


# # .88b  d88. d88888b d888888b db   db  .d88b.  d8888b. .d8888.
# # 88'YbdP`88 88'     `~~88~~' 88   88 .8P  Y8. 88  `8D 88'  YP
# # 88  88  88 88ooooo    88    88ooo88 88    88 88   88 `8bo.  
# # 88  88  88 88~~~~~    88    88~~~88 88    88 88   88   `Y8b.
# # 88  88  88 88.        88    88   88 `8b  d8' 88  .8D db   8D
# # YP  YP  YP Y88888P    YP    YP   YP  `Y88P'  Y8888D' `8888Y'


	def clearScreen(self):
		for i in range(30):
			print "\n",

	def showGame(self):
		self.clearScreen()
		print "-----------------------"
		print "***Jampack Blackjack***"
		print "-----------------------"
		print "\n\n"
		print self.message
		print "\n\n"
		print "Dealer's Hand: " + str(self.dealer.hand.value)
		self.dealer.hand.printHand() 
		print "\n\n\n"
		print "Player's Hand: " + str(self.player.hand.value)
		self.player.hand.printHand()
		print "\n\n"

	def printMe(self):
		self.player.printStats()
		self.player.printMe()
		self.dealer.printMe()
		print "Current number of cards left in deck: " + str(self.deck.size)

	def initialDeal(self):
		self.player.hand = Hand()
		self.dealer.hand = Hand()
		self.deck = Deck()
		self.player.bet = input("Place your bet! ")
		if self.player.bet > self.player.wallet:
			print "Cheater. Try again."
			self.player.bet = input("Place your bet!")
		self.message = "New Hand"
		self.dealer.hand.addCard(game.deck.dealMe())
		self.dealer.hand.addCard(game.deck.dealMe())
		self.player.hand.addCard(game.deck.dealMe())
		self.player.hand.addCard(game.deck.dealMe())

	def	playerTurn(self):
		hit = True
		while hit:
			choice = raw_input("Hit? y/n: ")
			if choice == "y":
				self.message = "Player Hits"
				self.showGame()
				time.sleep(1)
				self.player.hand.addCard(game.deck.dealMe())
				self.showGame()
				if self.player.hand.handFinished():
					hit = False
					break
			else:
				hit = False
				self.message = "End of Turn"
				self.showGame()

 	def dealerTurn(self):
	 	while self.dealer.hand.value < 17 or self.dealer.hand.value < self.player.hand.value:	 	 	
	 		if self.dealer.hand.value < self.player.hand.value and self.dealer.hand.handFinished() == False:	
					time.sleep(1)
					self.message = "Dealer Hits"
		 			self.showGame()
		 			time.sleep(1)
		 			self.dealer.hand.addCard(game.deck.dealMe())
		 			self.showGame()
		 			time.sleep(1)
		 	else: 
		 		break

	def roundOver(self):
		if self.player.hand.value > 21:
 			return True
 		elif self.dealer.hand.value > 21:
 			 return True
 		elif self.player.hand.hasBlackjack():
 			return True
 		elif self.dealer.hand.hasBlackjack():
 			return True
 		else:
 			return False

 	def declareOutcome(self):
 		if self.player.hand.value > 21:
 			self.player.wallet = self.player.wallet - self.player.bet
 			self.message = "Player Bust! You lose!"
 		elif self.dealer.hand.value > 21:
 			self.player.wallet = self.player.wallet + self.player.bet
 			self.message = "Dealer Bust! You win!"
 		elif self.player.hand.value == self.dealer.hand.value:
 			self.message = "It's a Tie! Weird."
 		elif self.player.hand.hasBlackjack():
 			self.player.wallet = self.player.wallet + (self.player.bet)*2
 			self.message = "You hit Blackjack! You win!!"
 		elif self.dealer.hand.hasBlackjack():
 			self.player.wallet = self.player.wallet - self.player.bet
 			self.message = "Dealer hit Blackjack! You lose!"
 		elif self.player.hand.value < self.dealer.hand.value:
 			self.player.wallet = self.player.wallet - self.player.bet
 			self.message = "You lose!!"
 		else:
 			self.message = "Weirdness happened."


 	def newHand(self):
 		global answer
 		print "You have $" + str(self.player.wallet)
		answer = raw_input("Would you like to play again? y/n: ")
		if answer != "y":
			self.player.wallet = 0


	def playAgain(self):
		global answer
		if answer == "y" and self.player.wallet <= 0:
			print "You are out of money. This will begin a new game."
			self.player.wallet = input("How much money you got? ")
			
# ooooooooooooo oooooooooooo  .oooooo..o ooooooooooooo  .oooooo..o
# 8'   888   `8 `888'     `8 d8P'    `Y8 8'   888   `8 d8P'    `Y8
#      888       888         Y88bo.           888      Y88bo.     
#      888       888oooo8     `"Y8888o.       888       `"Y8888o. 
#      888       888    "         `"Y88b      888           `"Y88b
#      888       888       o oo     .d8P      888      oo     .d8P
#     o888o     o888ooooood8 8""88888P'      o888o     8""88888P' 
#                                                               
#to test card constructor
# card1 = Card(0, 4)
# cardJack = Card(2, 11)
# cardAce = Card(0, 1)
# cardTen = Card(3, 10)

#to test hand constructor
# hand1 = Hand()
# hand1.addCard(cardTen)
# hand1.addCard(cardAce)
# hand1.printHand()
# print hand1.hasBlackjack()
# hand1.addCard(cardJack)
# hand1.printHand()
# print hand1.hasBlackjack()

#to test player constructor
# player = Player("jamie", 100)
# player.printStats()
# player.hand = blackjackHand
# player.printMe()

#to test deck constructor
# decktest = Deck()
# decktest.printDeck()

#has blackjack test
# blackjackHand = Hand()
# blackjackHand.addCard(decktest.dealMe())
# blackjackHand.addCard(decktest.dealMe())
# print blackjackHand.hasBlackjack()
# blackjackHand.printHand()
# decktest.printDeck()
# blackjackHand.printHand()

# testing the game constructor
# # game.printMe()
# game.player.hand.addCard(cardJack)
# game.player.hand.addCard(cardAce)
# game.player.hand.addCard(cardTen)
# game.dealer.hand.addCard(cardAce)
# # game.printMe()
# game.clearScreen()
# game.initialDeal()
# game.showGame()
# game.playerTurn()
game = Game()
answer = "y"
while game.player.wallet > 0:
	game.player.printStats()
	game.initialDeal()
	game.showGame()
	time.sleep(1)
	if not game.roundOver():
		game.playerTurn()
		if not game.roundOver():
			game.dealerTurn()
	game.declareOutcome()
	game.showGame()
	time.sleep(1)
	game.newHand()
	game.playAgain()


#hit 21 or went over test
# print game.player.hand.handFinished()
# print game.dealer.hand.handFinished()

