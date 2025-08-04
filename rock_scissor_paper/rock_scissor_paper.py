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
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK:'🪨',PAPER:'📃', SCISSORS:'✂️'}
def user_input():
	user_input= input("Rock,Paper,Scissor Enter (r | p | s) ?")
	if user_input not in [ROCK,PAPER,SCISSORS]:
		print("Invalid input")
	return user_input

def comp_input():
	comp_gen = random.choice([ROCK,PAPER,SCISSORS])
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
	print(f"Your choice is {emojis[user_data]}")
	print(f"Computer choice is {emojis[comp_data]}")
	if user_data == comp_data:
		print("It's a Draw")
		user_choice_check()	
	elif ((user_data == ROCK and comp_data == SCISSORS) or 
		 (user_data == SCISSORS and comp_data == PAPER) or 
		 ( user_data == PAPER and comp_data == ROCK)):
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
