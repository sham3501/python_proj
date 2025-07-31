# ask the input Rock, paper, scissors (r/p/s)
# check if its only r/p/s, other chars should be invalid.
# check if user Enters r, then computer should choose.

# Rock wins Scissor
# Scissor wins paper
# Paper wins Rock

# if you want to continue y/n if yes go to step1.
# else Print Thank you for playing
# go with cycle


import random

def user_input():
	user_input= input("Rock,Paper,Scissor Enter (r | p | s) ?")
	if user_input not in ['r','p','s']:
		print("Invalid input")
	return user_input

def comp_input():
	comp_gen = random.choice('rps')
	return comp_gen

def user_choice_check():
	user_choice = input("Do you want to continue to play y/n ? ").lower()
	if user_choice == 'y':
		play_rock_paper_scissor()
	elif user_choice == 'n':
		print("Thanks for playing !")
	else:
		print("Invalid input")
		user_choice_check()
	
def verify_user_comp(user_data, comp_data):
	print(f"Computer choice is {comp_data}")
	if user_data == comp_data:
			print("It's a Draw")
			user_choice_check()	
	elif (user_data == 'r' and comp_data == 's') or \
		 (user_data == 's' and comp_data == 'p') or \
		 ( user_data == 'p' and comp_data == 'r') :
		print("You Win")
		user_choice_check()
	else:
		print("You lost")
		user_choice_check()

def play_rock_paper_scissor():
	print("-- Welcome to Rock, Scissor, Paper Game!--")
	player = user_input()
	comp = comp_input()
	verify_user_comp(player,comp)
	
	
play_rock_paper_scissor()
