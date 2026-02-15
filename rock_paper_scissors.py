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

def get_player_move():
    move = input(color_blue + bold +
                 "Choose -> [r]ock, [p]aper or [s]cissors: " +
                 end_color).lower()

    if move == "r":
        return rock
    elif move == "p":
        return paper
    elif move == "s":
        return scissors
    else:
        print("Invalid input. Try again.")
        return None

def get_computer_move():
    computer_random_number = random.randint(1, 3)

    if computer_random_number == 1:
        return rock
    elif computer_random_number == 2:
        return paper
    elif computer_random_number == 3:
        return scissors

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "draw"

    if (player_move == rock and computer_move == scissors) or \
       (player_move == paper and computer_move == rock) or \
       (player_move == scissors and computer_move == paper):
        return "player"

    return "computer"

def show_round_result(player_move, computer_move, result):
    sleep(0.5)
    print(f"The computer chose -> {computer_move}")
    sleep(1)

    if result == "player":
        print(color_green + "You win!" + end_color)
    elif result == "computer":
        print(color_red + "You lose!" + end_color)
    else:
        print(color_yellow + "Draw!" + end_color)

def show_final_results(player_wins, computer_wins, draws):
    print("-------------------------------------")
    print(f"Your wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Draws: {draws}")

def main():
    player_wins = 0
    computer_wins = 0
    draws = 0

    print("Hello!\nThis is a simple Rock, Paper, Scissors game "
          "created by Dimitar Rusinov.\n"
          "Give it a try and see if you can outplay the machine.\n")

    while True:
        player_move = get_player_move()

        if player_move is None:
            continue

        computer_move = get_computer_move()

        result = determine_winner(player_move, computer_move)

        show_round_result(player_move, computer_move, result)

        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
        else:
            draws += 1

        try_again = input("Play again? [yes/no]: ").lower()

        if try_again != "yes":
            if try_again == "no":
                break
            sleep(0.3)
            print("Invalid answer, try again...")
            sleep(0.4)
            try_again = input(f"{end_color}Type {end_color}[{color_green}yes{end_color}] to {bold}play again{end_color} or [{color_lred}no{end_color}] to {bold}quit{end_color}: ").lower()

    sleep(0.5)
    result_check = input(
        "Do you want to check the results [yes/no]? ").lower()

    if result_check == "yes":
        show_final_results(player_wins, computer_wins, draws)

if __name__ == "__main__":
    main()
