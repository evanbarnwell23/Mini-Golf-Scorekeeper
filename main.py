# Evan Barnwell
# Integration Project
# MiniGolf Scorekeeper
# This program keeps score of a game of MiniGolf.
# The program supports up to 9 holes and up to 4 players.
# The program prints player scores at the end of the game.

def print_gap():  # This function prints a 'gap' to separate parts of the scorekeeper for readability
    print('.')
    print('.')
    print('.')

def print_bar():  # This function prints a 'bar' to separate parts of the scorekeeper for readability
    print('------------------------------------------------------------------------')

def print_intro():  # This function prints the introduction the the scorekeeper
    print("Welcome to Dorm MiniGolf Scorekeeper!")
    input('Press enter to begin: ')
    print_gap()

def get_holes():  # This function gets the number of holes the user would like to score
    print('Please enter the number of holes you would like to play: ')
    for hole in range(1, 10):  # Prints choices for number of holes in multiple choice fashion
        print(f'({hole}) {hole}', end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            holes = int(input())
        except ValueError:
            print_gap()
            print('Please enter a number between 1 and 9: ')
        else:
            break
    return holes  # Returns an amount of holes

def make_holes_list(holes):  # This function makes the holes into a list
    holes_list = list(range(1, holes + 1))
    return holes_list

def check_hole_count():  # This function ensures the user entered a valid number of holes
    print_gap()
    print('Please enter a number between 1 and 9: ')
    for hole in range(1, 10):  # Prints choices for number of holes in multiple choice fashion
        print(f'({hole}) {hole}', end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            holes = int(input())
        except ValueError:
            print_gap()
            print('Please enter a number between 1 and 9: ')
        else:
            break
    return holes  # Returns an amount of holes

def get_player_count():  # This function gets the number of players the user would like to score
    print_gap()
    print('Please enter the number of players: ')
    for player in range(1, 5):  # Prints choices for number of holes in multiple choice fashion
        print(f'({player}) {player}', end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            players = int(input())
        except ValueError:
            print('Please enter an integer between 1 and 4: ')
        else:
            break
    return players  # Returns an amount of players

def check_player_count():  # This function ensures the user entered a valid number of players
    print_gap()
    print('Please enter a number between 1 and 4: ')
    for player in range(1, 5):  # Prints choices for number of holes in multiple choice fashion
        print(f'({player}) {player}', end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            players = int(input())
        except ValueError:
            print_gap()
            print('Please enter a number between 1 and 4: ')
        else:
            break
    return players  # Returns an amount of players

def get_player_names(players):  # This function gets the names of the players
    print_gap()
    player_names = []  # List that player names are stored in
    for player in range(1, players + 1):  # Loop to get player names base on number of players being scored
        player_names.append(input(f'Enter the name of Player {player}: '))
    return player_names  # Returns the list of player names

def make_player_list(player_count, player_names):  # This function creates a list of the players
    player_list = []
    for player in range(1, player_count + 1):  # Loop creating players as elements of the list
        player_list.append([player_names[player - 1], []])  # Each player/element of the list is a tuple
    return player_list  # Returns the list of players

def sort_players(player_list):  # This function sorts players based on their score (second element of the tuple)
    sorted_list = sorted(player_list, key=lambda tup: tup[1])  # Sort taken from
    # https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    return sorted_list  # Returns the player list sorted

def make_live_scoreboard(sorted_list):  # This function prints a live scoreboard while the game is running
    places = ['1st', '2nd', '3rd', '4th']  # List of places to be entered in the live scoreboard
    print('Scoreboard:')
    print_bar()
    for player in range(0, len(sorted_list)):  # Loop that creates scoreboard depending on number of players
        print(f'{sorted_list[player][0]} is in {places[player]} place with a score of {sum(sorted_list[player][1])}!')
    print_bar()

def get_scores(holes, players, player_list, holes_list):  # This function gets player scores
    holes_played = 0
    for hole in range(0, holes):  # Loop for number of holes
        print_gap()
        print(f'Hole {(hole + 1)}: ')
        print_bar()
        for player in range(0, players):  # Loop for number of players
            print(f"Enter {player_list[player][0]}'s score on hole {str(holes_list[hole])}: ")
            while True:  # Makes sure the user enters a valid input
                try:
                    player_input = int(input())
                except ValueError:
                    print('Please enter an integer.')
                else:
                    break
            player_list[player][1].append(player_input)  # Adds the input to the appropriate player's score in the
            # player list
        if holes_played < holes - 1:  # Makes the live scoreboard not be printed on the last hole
            sorted_list = sort_players(player_list)
            make_live_scoreboard(sorted_list)
            holes_played += 1
    print_bar()
    print('The game is finished!')
    input('Press enter to see who won! ')
    return player_list

def make_final_list(players, player_list):  # This function creates a final list once the game has finished
    final_list = []
    for player in range(0, players):
        player = (player_list[player][0], sum(player_list[player][1]))  # Sums the list of scores so it can be displayed
        final_list.append(player)
    return final_list

def make_scoreboard(sorted_list):  # This function makes the final scoreboard displayed at the end of the game
    places = ['1st', '2nd', '3rd', '4th']  # List of places to be entered in the live scoreboard
    print_gap()
    print('Scoreboard:')
    print_bar()
    for player in range(0, len(sorted_list)):  # Loop that creates scoreboard depending on number of players
        print(f'{sorted_list[player][0]} came in {places[player]} place with a score of {(sorted_list[player][1])}!')
    print_bar()
    input('Press enter to continue. ')

def write_to_file(final_list, player_count):  # This function writes to a text file where games are scored
    bar = '---------------------------'
    n = '\n'
    file = open('scorekeeper.txt', 'a')  # Opens (or creates) the file in append mode
    file.write(bar)
    file.write(n)
    for player in range(player_count):  # Loop to write each player and their score
        file.write('Player: ' + final_list[player][0])
        file.write(n)
        file.write('Score: ' + str(final_list[player][1]))
        file.write(n)
    file.write(bar)
    file.write(n)
    file.close()

def play_again():  # This function asks the user if it would like to play again
    print_gap()
    check = True
    again = True
    while check:  # Will continue to check if the user enters a value other than 1 or 2
        print('Would you like to play again?')
        print('Press (1) for yes or (2) for no: ')
        while True:
            try:  # Makes sure user input is valid
                again_key = int(input())
            except ValueError:
                print('Please enter 1 or 2.')
            else:
                break
        if again_key == 1:
            print_gap()
            again = True
            check = False
        elif again_key == 2:
            again = False
            check = False
        else:
            check = True
    return again  # Returns boolean for whether or not the program will run again

def print_outro():  # This function prints the print_outro to the scorekeeper
    print_gap()
    print('Goodbye!')

def main():  # This is the main function
    playing = True
    while playing:
        print_intro()
        hole_count = get_holes()
        holes_list = make_holes_list(hole_count)
        while hole_count > 9 or hole_count < 1:  # Checks hole count if user entered a value that was out of range
            hole_count = check_hole_count()
        player_count = get_player_count()
        while player_count > 4 or player_count < 1:  # Checks player count if user entered a value that was out of range
            player_count = check_player_count()
        player_names = get_player_names(player_count)
        player_list = make_player_list(player_count, player_names)
        player_list = get_scores(hole_count, player_count, player_list, holes_list)
        final_list = make_final_list(player_count, player_list)
        sorted_list = sort_players(final_list)
        make_scoreboard(sorted_list)
        write_to_file(final_list, player_count)
        playing = play_again()
    print_outro()

# CALL TO MAIN #
main()
