print("hello")

print("dishant")

import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = input("Choose rock, paper, or scissors: ").lower()

if player == computer:
    print("It's a tie!")
elif (player == 'rock' and computer == 'scissors') or \
     (player == 'paper' and computer == 'rock') or \
     (player == 'scissors' and computer == 'paper'):
    print(f"You win! Computer chose {computer}.")
else:
    print(f"Computer wins! It chose {computer}.")