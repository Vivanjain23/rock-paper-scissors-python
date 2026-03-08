import random
'''
=====🎮 ROCK PAPER SCISSORS GAME 🎮=====
************* GAME RULES ****************

1. Rock beats Scissors
2. Scissors beats Paper
3. Paper beats Rock
4. If both choices are same → Tie

'''
choices = ["rock" , "paper" , "scissors"]

player_score = 0
computer_score = 0
round = 1

while True:
    print(f"\n******** Round {round} ********")

    player = input("Enter rock, paper, or scissors: ").lower()

    if(player not in choices):
        print("Invalid choice")
        print("Try again!")
        continue

    computer = random.choice(choices)
    print(f"Computer chose {computer}")

    if(computer == player):
        print("It's a tie!")
    elif(player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        print("You win this round!")
        player_score+=1
    else:
        print("Computer win this round!")
        computer_score+=1

    #Score display
    print("\n----SCORE----")
    print("Player score: ",player_score)
    print("Compuer score: ",computer_score)

    #ask to continue
    play_again = input("\nWanna play another round? (yes/no): ").lower()
    
    if(play_again != "yes"):
        break
    round+=1

print("\n======= Final Score =======")
print("Player score: ",player_score)
print("Compuer score: ",computer_score)

if(player_score > computer_score):
    print("You are overall winner!")
elif(computer_score > player_score):
    print("Computer wins the game!")
else:
    print("It's a Draw!")


print("\n------THANKS FOR PLAYING------")
