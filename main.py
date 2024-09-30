from random import randint

fire = "🔥"

def roll_dice():
	dices_amount = input('How many dices do You have?')
	rolled_amount = 0
	
	i = 1
	while i < int(dices_amount):
		rolled_number = randint(1, 6)
		rolled_amount += rolled_number
		i += 1
	
	print('You rolled a', rolled_amount, fire*rolled_amount)

roll_dice()
