# 1. Randomly generate numbers between 1-100
# 2. Ask the player to guess the Number
# 3. give a hint, if the number is higher the guess or lower the guess

import random
def number_guess():
	try:
		print("Welcome to number guessing Game!")
		random_num = random.randint(1,100)
		print("I got My Number")
		print("You have 5 attempts to guess")
		user_num = int(input("Guess the number between 1 to 100 ? "))
		count_guess = 0
		attempts = 5
		while attempts > 0:
			attempts -=1
			count_guess +=1
			
			if user_num == random_num:
				print(f"You got the correct guess!! took {count_guess} attempts")
				break
			elif user_num < random_num:
				print("Your Guess is lower than My number")
				user_num = int(input("Guess the number again? "))
			else:
				print("Your guess is higher than My number")
				user_num = int(input("Guess the number again ? "))
				
			if attempts == 0:
				print(f"You exausted the attemts, My number is {random_num}!")
				break
			else:
				print(f"You left with {attempts} attempts")

	except ValueError:
		print("Invalid Input, enter the numbers between 1 to 100")
			

number_guess()
