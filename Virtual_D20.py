import random
import time
print("Welcome to the virutal D20!")
print("Wizards, Shamans and Warriors alike, what shall the RNG gods generate for you today?")
print("Tip: You can add a number to the front of your user_roll for multiple roles! (eg. 3d6)")

def check_valid(n):
    scrap, roll_check = user_roll.split('d')
    if roll_check not in check_list:
        str.x = 69 #Check if user input is valid, if not, throw TypeError.
def roll_dice(n):
    if user_roll[0] != 'd':
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
    check_list = ['4', '6', '8', '10', '00', '12', '20']
    print('                D4 | D6 | D8 | D10 | D00 | D12 | D20 or Q to quit')
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
            if modifier != 0:
                user_roll.append(modifier)
                user_roll = sum(user_roll)
                print('Your rolls and modifier equal: ', user_roll)
        except (ValueError, TypeError):
            print("I don't understand that roll.\n")
            
print("Thanks for using The Virtual D20, stay strong Adventurer!")
