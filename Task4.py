"""
Task 4 Rock Paper Scissors Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.
Remember the rules: # - Rock beats scissors # - Scissors beats paper # - Paper beats rock
"""

options = """
Please select of the options below
1. Rock
2. Scissors
3. Paper
"""


def get_winner(player1_input, player2_input):
    """Logic to find winner - p1_win_scenarios dictionary contains player 1 selected option as key and scenarios
    player 1 wins when player 2 selected options present in dictionary values
    """
    p1_win_scenarios = {
        1: [2],
        2: [3],
        3: [1]
    }
    if player1_input == player2_input:
        return 0
    elif player2_input in p1_win_scenarios[player1_input]:
        return 1
    else:
        return 2


def get_options():
    return options


def main():
    print("### Rock Paper Scissors Game ###")
    player1_name = input("Enter Name of Player 1 : ")
    player2_name = input("Enter Name of Player 2 : ")
    try:
        user_input = input("Do you want to play? Enter 1 to Start Game, 2 to End Game ")
        while user_input not in ['1', '2']:
            print("Invalid Option")
            user_input = input("Do you want to play? Enter 1 to Start Game, 2 to End Game ")
        user_input = int(user_input)
        while user_input != 2:
            if user_input == 1:
                print(get_options())
                player1_input = input(f"PLease enter {player1_name}'s option ")
                while player1_input not in ['1', '2', '3']:
                    print("Invalid Option")
                    player1_input = input(f"PLease enter {player1_name}'s option ")
                player2_input = input(f"PLease enter {player2_name}'s option")
                while player2_input not in ['1', '2', '3']:
                    print("Invalid Option")
                    player2_input = input(f"PLease enter {player2_name}'s option ")
                player1_input = int(player1_input)
                player2_input = int(player2_input)
                winner = get_winner(player1_input, player2_input)
                if winner == 1:
                    print(f"{player1_name} Won")
                elif winner == 2:
                    print(f"{player2_name} Won")
                else:
                    print("Game is Draw")
            else:
                print("Invalid CHoice")
            user_input = input("Do you want to play? Enter 1 to Start Game, 2 to End Game ")
            while user_input not in ['1', '2']:
                print("Invalid Option")
                user_input = input("Do you want to play? Enter 1 to Start Game, 2 to End Game ")
            user_input = int(user_input)
    # Catching valueError to handle invalid user inputs which crashes program due to failure of type casting to integer
    except ValueError:
        print("Invalid Input")
    print("Game Over")


if __name__ == "__main__":
    main()
