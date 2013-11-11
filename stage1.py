import random
def shuffled_deck():
	deck=[]
	for suit in ['club','heart','diamond','spade']:
		for num in xrange(1,15):
			deck.append([suit,num])
	random.shuffle(deck)
	return deck
def name(card):
	if card==11:
		return 'jack'
	elif card==12:
		return 'queen'
	elif card==13:
		return 'king'
	elif card==1:
		return 'ace'
	else:
		return str(card)
	
