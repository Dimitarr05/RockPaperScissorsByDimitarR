import random
from time import sleep

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
color_red = '\033[31m'
color_lred = '\033[1;31m'
color_green = '\033[32m'
color_blue = '\033[36m'
bold = '\033[1m'
color_yellow = '\033[33m'
end_color = '\033[0m'

player_wins = 0
computer_wins = 0
draws = 0

print("Hello!\nThis is a simple Rock, Paper, Scissors game created by Dimitar Rusinov.\nIt’s a small project built for practice and a bit of fun — nothing complicated, just clean logic and a quick challenge against the computer.\nGive it a try and see if you can outplay the machine. 😉\n")

while True:
    player_move = input (color_blue + bold + "Choose -> [r]ock, [p]aper or [s]cissors: " + end_color)
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Please, try again...")

    computer_random_number = random.randint(1,3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    sleep(0.5)
    print(f"The computer chose -> {computer_move}")
    sleep(1.1)
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(color_green + "You win!")
        player_wins += 1
    elif player_move == computer_move:
        print(color_yellow + "Draw!")
        draws += 1
    else:
        print(color_red + "You lose!")
        computer_wins += 1
    sleep(1)
    try_again = input(f"{end_color}Type {end_color}[{color_green}yes{end_color}] to {bold}play again{end_color} or [{color_lred}no{end_color}] to {bold}quit{end_color}: ")
    if try_again == "yes":
        continue
    elif try_again == "no":
        sleep(0.5)
        print("Thank you for playing! :)")
        break
    else:
        raise SystemExit("Invalid input. Please, try again...")
sleep(0.5)
result = input("-------------------------------------\nDo you want to check the results [yes/no]? ")
if result == "yes":
    sleep(1.5)
    print("-------------------------------------")
    print(f"Your wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Draws: {draws}")