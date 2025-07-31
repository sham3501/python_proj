# 1. Randomly generate numbers between 1-100
# 2. Ask the player to guess the Number
# 3. give a hint, if the number is higher the guess or lower the guess

import random
def number_guess():
	print("Welcome to number guessing Game!")
	random_num = random.randint(1,100)
	print("I got My Number")
	print("You have 5 attempts to guess")
	user_num = int(input("Guess the number between 1 to 100 ? "))
	count_guess = 0
	attempts = 5
	while attempts > 1:
		attempts -=1
		count_guess +=1
		print(f"You left with {attempts} attempts")
		if  user_num > random_num:
			print("Your guess is higher than My number")
			user_num = int(input("Guess the number again ? "))
		elif user_num < random_num:
			print("Your Guess is lower than My number")
			user_num = int(input("Guess the number again? "))
		else:
			print(f"You got the correct guess!! took {count_guess} attempts")
			break

	else:
		print(f"You exausted the attemts, My number is {random_num}!")
		

number_guess()
