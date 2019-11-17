import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask player to guess 6 times
for guessTaken in range(1, 7):
  print('Take a guess, you have six tries.')
  guess = int(input())

  if guess < secretNumber:
    print('Your guess is too low.')
  elif guess > secretNumber:
    print('Your guess is too high')
  else:
    break # This condition is the correct guess


if guess == secretNumber:
  print(f'Good job! You guessed my number in {guessTaken} guesses!')
else:
  print(f'Nope. The number i was thinking about was {secretNumber}.')
  

