import random
def get_winner(player,computer):
    if player==computer:
        return "Game is tied"
    elif (player=="rock" and computer=="scissors")or\
        (player=="paper" and computer=="rock")or\
        (player=="scissors" and computer=="paper"):
        return "player won"
    else:
        return "computer won"
choices=["rock","paper","scissors"]
print("rock paper scissors game")
print("Choose rock,paper or scissors")
while True:
    player_choice=input("\n Your Choice: ").lower()
    if player_choice not in choices:
        print("Invalid choice, Try Again")
        continue
    computer_choice=random.choice(choices)
    print(f"Computer Choice: {computer_choice}")
    result=get_winner(player_choice ,computer_choice)
    print(result)
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! ")
        break

    
    