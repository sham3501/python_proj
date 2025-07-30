# Ask the user whether user wants to play the Dice game
	# If user wants to play : y
		# Create two random numbers
		# print them
	# If user Enters a number
		# Print thank you message
		# Terminate
	# Else print Invalid choice

# Enhance, how many times user wants to roll the dice

import random 

def roll_dice():
	print("Welcome to Dice Game !")
	roll_num = 0
	while True:
		choice = input("Roll the dice y/n ?").lower()
		if choice == 'y':
			die1 = random.randint(1,6)
			die2 = random.randint(1,6)
			print(f"({die1}, {die2})")
			roll_num +=1
			print(f"Dice rolled {roll_num} times")
		elif choice == 'n':
			print("Thank you for playing !")
			break
		else:
			print("Invalid choice")
	print(f"Total dice rolled {roll_num} times")
	
roll_dice()
