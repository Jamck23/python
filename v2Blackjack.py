#Blackjack - Second Try! (March 12, 2013)
#Successful, needs cleaning + revamps!
import random
import time

#  .o88b. db       .d8b.  .d8888. .d8888. d88888b .d8888.
# d8P  Y8 88      d8' `8b 88'  YP 88'  YP 88'     88'  YP
# 8P      88      88ooo88 `8bo.   `8bo.   88ooooo `8bo.  
# 8b      88      88~~~88   `Y8b.   `Y8b. 88~~~~~   `Y8b.
# Y8b  d8 88booo. 88   88 db   8D db   8D 88.     db   8D
#  `Y88P' Y88888P YP   YP `8888Y' `8888Y' Y88888P `8888Y'

#Card constructor
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

# cardOne = Card("Clubs", 12)
# print cardOne.family, cardOne.rank, cardOne.value	// tests Card constructor

# #Deck of Cards constructor
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

# deckOne = Deck()				#tests Deck constructor
# deckOne.printDeck()
# print deckOne.size

#Hand Constructor (tracks cards dealt)
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

# playHand = Hand(playHand)
# cardOne = deckOne.cardList[12]
# cardOne.printCard()
# cardTwo = deckOne.cardList[24]
# cardTwo.printCard()
# playHand.addCard(cardOne)
# playHand.addCard(cardTwo)
# playHand.printHand()
# print playHand.value



#  d888b   .d8b.  .88b  d88. d88888b
# 88' Y8b d8' `8b 88'YbdP`88 88'    
# 88      88ooo88 88  88  88 88ooooo
# 88  ooo 88~~~88 88  88  88 88~~~~~
# 88. ~8~ 88   88 88  88  88 88.    
#  Y888P  YP   YP YP  YP  YP Y88888P

def game():
	global bet
	global wallet
	global activeDeck
	while wallet > 0: 
		activeDeck = Deck()
		playerHand = Hand("Player")
		dealerHand = Hand("Dealer")
		bet = input("Place your bet! ")
		print "Dealer's Hand: "
		initialDeal(dealerHand)
		print "Player's Hand: "
 		initialDeal(playerHand) 
 		if stopGame(dealerHand) == False or stopGame(dealerHand) == True and result == 2:
			if stopGame(playerHand) == False:
				interact(playerHand) 
				if stopGame(playerHand) == False or stopGame(playerHand) == True and result == 1:
					dealerTurn(dealerHand)
					stopGame(dealerHand)
		declareOutcome(playerHand, dealerHand)               #changes wallet value
		print "You now have $" + str(wallet)
		if wallet > 0:
	 		newHand() 

	print "Game Over. Thanks!"

# .88b  d88. d88888b d888888b db   db  .d88b.  d8888b. .d8888.
# 88'YbdP`88 88'     `~~88~~' 88   88 .8P  Y8. 88  `8D 88'  YP
# 88  88  88 88ooooo    88    88ooo88 88    88 88   88 `8bo.  
# 88  88  88 88~~~~~    88    88~~~88 88    88 88   88   `Y8b.
# 88  88  88 88.        88    88   88 `8b  d8' 88  .8D db   8D
# YP  YP  YP Y88888P    YP    YP   YP  `Y88P'  Y8888D' `8888Y'

def initialDeal(hand):
	global activeDeck
	deal(hand)
	deal(hand)
	hand.printHand()
	print "Value: " + str(hand.value)


def deal(hand):
	global activeDeck
	pick = random.randrange(1, activeDeck.size)
	card = activeDeck.cardList[pick]
	hand.addCard(card)
	activeDeck.cardList.pop(pick)
	activeDeck.adjustDeck()

	
def stopGame(hand):
	global result
	if hand.value == 21:
		if hand.hasAce and hand.hasJack:
			if hand.name == "Player":
				result = 5
			elif hand.name == "Dealer":
				result = 6
		else:
			if hand.name == "Player":
				result = 1
			elif hand.name == "Dealer":
				result = 2
		return True
	elif hand.value > 21:
		if hand.name == "Player":
			result = 2
		elif hand.name == "Dealer":
			result = 3
		return True
	else:
		result = 0
		return False

def interact(hand):
	global result
	hit = True
	while hit == True:
		choice = raw_input("Hit? y/n: ")
		if choice == 'y':
			deal(hand)
			hand.printHand()
			print "Value: " + str(hand.value)
			if stopGame(hand) == True:
				hit = False
				break
		else:
			hit = False
			print "End of Turn"

def dealerTurn(hand):
	while hand.value < 17:
		time.sleep(1)
		print "Dealer Hits"
		time.sleep(1)
		deal(hand)
		hand.printHand()
		print "Value: " + str(hand.value)


def declareOutcome(handP, handD):
	global result
	global wallet
	global bet
	if result == 1:    #Player hit 21
		wallet = wallet + bet
		print "You hit 21! Congratulations!"
	elif result == 2:  #Dealer hit 21 or Player went over
		wallet = wallet - bet
		print "You Lose!!"
	elif result == 3:   #Dealer went over, player stayed under
		wallet = wallet + bet
		print "Dealer went over! You win!"
	elif result == 4:   #Dealer hits Blackjack
		wallet = wallet - bet
		print "Blackjack!! You Lose."
	elif result == 5:    #Player hits Blackjack
		wallet = wallet + bet*1.5
		print "Blackjack!! You Win!!"
	elif result == 0:
		if handD.value == handP.value:
			print "A tie! What are the odds?!" 
		elif handD.value > handP.value:
			print "Dealer Wins! You were too low."
			wallet = wallet - bet
		elif handP.value > handD.value:
			print "You Win! Congratulations!"
			wallet = wallet + bet

def newHand():
	global wallet
	answer = raw_input("You've got money left! Play again? y/n: ")
	if answer != "y":
		wallet = 0


def newGame():
	global wallet
	global gamePlay
	answer = raw_input("Would you like to try again? y/n: ")
	if answer == "y":
		gamePlay = True
	else:
		gamePlay = False

# testHand = Hand()
# deckTest = Deck()

# initialDeal(testHand)
# interact(testHand)
# testHand.printHand()
# deckTest.printDeck()
# print deckTest.size
# testHand.printHand()
# deal(testHand)
# print deckTest.size
# testHand.printHand()
# deal(testHand)
# print deckTest.size
# testHand.printHand()
# deckTest.printDeck()
# print deckTest.size
# initialDeal(testHand)
gamePlay = True
while gamePlay == True:
	activeDeck = Deck()
	playerHand = Hand("Player")
	dealerHand = Hand("Dealer")
	result = 0
	wallet = input("Welcome to Blackjack! How much money you got? ")
	bet = 0
	game()
	if wallet <= 0:
		newGame() #re-calls game() and starts over
