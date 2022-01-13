# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == 'r':
	if computer_choice == 'p':
		print('Computer chose paper, you lost')
	elif computer_choice == 's':
		print('Computer chose scissors, you won')
	elif computer_choice == 'r':
		print('Computer chose rock, is a tie')
elif user_choice == 'p':
	if computer_choice == 'p':
		print('Computer chose paper, is a tie')
	elif computer_choice == 's':
		print('Computer chose scissors, you lost')
	elif computer_choice == 'r':
		print('Computer chose rock, you won')
elif user_choice == 's':
	if computer_choice == 'p':
		print('Computer chose paper, you won')
	elif computer_choice == 's':
		print('Computer chose scissors, is a tie')
	elif computer_choice == 'r':
		print('Computer chose rock, you lost')