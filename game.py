class Character():
	''' Base class for a character. '''
	turn_mana = 0
	health = 1
	is_alive = True
	
	def __init__(self, name, health, turn_mana):
		self.cards = []
		self.name = name
		self.health = health
		self.turn_mana = turn_mana
	
	def add_card(self, card):
		''' Adds a card to the players card inventory '''
		self.cards.append(card)

	def attack(self, card, enemy):
		''' Each character can attack the enemy. The damange that
		comes from the card will be dealt unto the enemy. '''
		damage = card.damage
		enemy.health -= damage
		if enemy.health <= 0:
			enemy.death()
	
	def death(self):
		''' If health reaches 0 then this character died. '''
		print("Oh no died.")
		self.is_alive = False

class Hero(Character):
	''' The hero class. This is the class that the player will use. '''		
	
	def __init__(self, name, health, turn_mana):
		super().__init__(name, health, turn_mana)

class Enemy(Character):
	''' The enemy class. This is the class that the player will slay. '''
	
	def __init__(self, name, health, turn_mana):
		super().__init__(name, health, turn_mana)

class Card():
	'''
	The base class for a card.
	Only has damage and mana use.
	''' 
	damage = 0
	mana = 0

	def __init__(self, name, mana):
		self.name = name
		self.mana = mana

class MeleeCard(Card):
	''' Child of the Card class, is melee. '''	
	type = 'Melee'

	def __init__(self, name, damage, mana, effect=None):
		''' A melee card, physical damage. ''' 
		super().__init__(name, mana)
		self.damage = damage
		self.effect = effect

class HealCard(Card):
	'''
	Increases health of the character that it is used on.
	'''

	type = 'Heal'

	def __init__(self, name, mana, heal_amt):
		super().__init__(name, mana)
		self.heal_amt = heal_amt

	

# For testing purposes.
luna = Hero('Luna', 100, 10)
stinky = Enemy('Stinky', 15, 5)
banana = MeleeCard('Banana', 10, 2)
