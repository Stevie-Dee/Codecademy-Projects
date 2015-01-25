from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
print 'Pick a number between 1 and 10'
while guesses_left > 0:
	guess = int(raw_input("Your guess: "))
	if guess == random_number:
		print 'You win!'
		break
	guesses_left -= 1

else:
	print 'You lose.'
