import random
import time
print("Welcome to the virutal D20!")
print("Wizards, Shamans and Warriors alike, what shall the RNG gods generate for you today?")
print("Tip: You can add a number to the front of your user_roll for multiple roles! (eg. 3d6)")

def check_valid(n):  #Check if user input is valid, if not, throw TypeError.
	check_list = ['4', '6', '8', '10', '00', '12', '20'] # List of valid inputs
	scrapValue, roll_check = user_roll.split('d') #scrapValue variable used to placehold any input before 'd'
	if roll_check not in check_list:
		str.x = 69 
def roll_dice(n): # Function to roll dice.
	if user_roll[0] != 'd': # If first character of input is not d, user is rolling multiple die.
		numberOfDie, die = user_roll.split('d')
		if (int(die) == 0): # Special case for D00 Roles, only available rolls are percentiles from 00 - 90
			return [(random.randint(0, 9) * 10) for n in range(int(numberOfDie))]
		elif int(die) == 10: # Special case where die starts at 0 and ends at 9
			return [random.randint(0, 9) for n in range(int(numberOfDie))]
		else: # Normal dice rolls 1 - dice number
			return [random.randint(1, int(die)) for n in range(int(numberOfDie))]
	else: # Single dice roll
		scrapValue, die = user_roll.split('d') #scrapValue variable used to placehold unwanted value from split.
		if (int(die) == 0): # Special case for D00 Roles, only available rolls are percentiles from 00 - 90
			return [random.randint(0, 9) * 10]
		elif int(die) == 10: # Special case where die starts at 0 and ends at 9
			return [random.randint(0, 9)]
		else: 
			return [random.randint(1, int(die))]

while True:
	print('                D4 | D6 | D8 | D10 | D00 | D12 | D20 or Q to quit') # Awkward way to format print, justification wasn't working.
	user_roll = input()
	user_roll = user_roll.lower()
	if user_roll == 'q': # Escape while loop when user decides to quit
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
