import random
import time
print("Welcome to the virutal D20!")
print("Wizards, Shamans and Warriors alike, what shall the RNG gods generate for you today?")
print("Tip: You can add a number to the front of your user_roll for multiple roles! (eg. 3d6)")

def check_valid(n):  #Check if user input is valid, if not, throw TypeError.
	check_list = ['4', '6', '8', '10', '00', '12', '20'] # List of valid inputs
	scrap, roll_check = user_roll.split('d') #scrap variable used to hold any input before 'd'
	if roll_check not in check_list:
		str.x = 69 
def roll_dice(n): # Function to roll dice.
	if user_roll[0] != 'd': # If first character of input is not d, dice roll will be a multi-roll.
		number, die = user_roll.split('d')
		if (int(die) == 0):
			return [(random.randint(0, 9) * 10) for n in range(int(number))]
		elif int(die) == 10:
			return [random.randint(0, 9) for n in range(int(number))]
		else:
			return [random.randint(1, int(die)) for n in range(int(number))]
	else:
		scrap, die = user_roll.split('d') #scrap variable used to placehold unwanted value from split.
		if (int(die) == 0):
			return [random.randint(0, 9) * 10]
		elif int(die) == 10:
			return [random.randint(0, 9)]
		else:
			return [random.randint(1, int(die))]

while True:
	print('                D4 | D6 | D8 | D10 | D00 | D12 | D20 or Q to quit') # Awkward way to format print, justification wasn't working.
	user_roll = input()
	user_roll = user_roll.lower()
	if user_roll == 'q':
	   break
	else:
		try:
			modifier = input('Modifier? Pos/neg number or leave blank\n')
			if modifier == '': #Check if input for modifier is empty, if so, assign to 0 for sum later.
				modifier = 0
			modifier = int(modifier)
			check_valid(user_roll)
			print('May your die roll true...')
			time.sleep(2)
			user_roll = roll_dice(user_roll)
			print(user_roll)
			if modifier != 0: # If user entered modifier, add to final output.
				user_roll.append(modifier)
				user_roll = sum(user_roll)
				print('Your rolls and modifier equal: ', user_roll)
		except (ValueError, TypeError): # Catch any incorrect input from user.
			print("I don't understand that roll.\n")
			
print("Thanks for using The Virtual D20, stay strong Adventurer!")
print("Created by Aaron Lewis. Github.com/AaronL1011")
