# Roll two dice until your total score reaches or exceeds 30.
# Each round, the player rolls two dice.
# The sum of the two dice is added to the total score.
# You can choose to continue or stop after each roll.
# If you reach exactly 30, you win.
# If you go over 30, you lose.
# If you quit before reaching 30, the game ends.
import random
def dice_enhanced():
	print("Welcome to Dice Game!")
	total_score = 0
	#roll_count = 0
	while True:
		choice = input("Roll the dice y/n ? ").lower()
		if choice == 'y':
			die1 = random.randint(1,6)
			die2 = random.randint(1,6)
			score = die1 + die2
			total_score += score
			print(f"total_score {total_score}")
			if total_score == 30:
				print("You Win !")
				break
			elif total_score > 30:
				print("You lost")
				break
		elif choice == 'n' and total_score < 30:
			print("Thank you for playning! Game Ends!")
			break
		else:
			print("Invalid choice")
		
		
dice_enhanced()