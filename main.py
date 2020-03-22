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
        print('(' + str(hole) + ')', str(hole), end='  ')
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
    holesList = list(range(1, holes + 1))
    return holesList

def check_hole_count(holes):  # This function ensures the user entered a valid number of holes
    print_gap()
    print('Please enter a number between 1 and 9: ')
    for hole in range(1, 10):  # Prints choices for number of holes in multiple choice fashion
        print('(' + str(hole) + ')', str(hole), end='  ')
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
        print('(' + str(player) + ')', str(player), end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            players = int(input())
        except ValueError:
            print('Please enter an integer between 1 and 4: ')
        else:
            break
    return players  # Returns an amount of players

def check_player_count(players):  # This function ensures the user entered a valid number of players
    print_gap()
    print('Please enter a number between 1 and 4: ')
    for player in range(1, 5):  # Prints choices for number of holes in multiple choice fashion
        print('(' + str(player) + ')', str(player), end='  ')
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
    playerNames = []  # List that player names are stored in
    for player in range(1, players + 1):  # Loop to get player names base on number of players being scored
        playerNames.append(input('Enter the name of Player ' + str(player) + ': '))
    return playerNames  # Returns the list of player names

def make_player_list(playerCount, playerNames):  # This function creates a list of the players
    playerList = []
    for player in range(1, playerCount + 1):  # Loop creating players as elements of the list
        playerList.append([playerNames[player - 1], []])  # Each player/element of the list is a tuple
    return playerList  # Returns the list of players

def sort_players(playerList):  # This function sorts players based on their score (second element of the tuple)
    sortedList = sorted(playerList, key=lambda tup: tup[1])  # Sort taken from
    # https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    return sortedList  # Returns the player list sorted

def make_live_scoreboard(sortedList):  # This function prints a live scoreboard while the game is running
    places = ['1st', '2nd', '3rd', '4th']  # List of places to be entered in the live scoreboard
    print('Scoreboard:')
    print_bar()
    for player in range(0, len(sortedList)):  # Loop that creates scoreboard depending on number of players
        print(sortedList[player][0], 'is in', places[player], 'place with a score of', str(sum(sortedList[player][1])) +
              '!')
    print_bar()

def get_scores(holes, players, playerList, holesList):  # This function gets player scores
    holesPlayed = 0
    for hole in range(0, holes):  # Loop for number of holes
        print_gap()
        print('Hole', str(hole + 1) + ': ')
        print_bar()
        for player in range(0, players):  # Loop for number of players
            print('Enter', playerList[player][0] + "'s score on hole", str(holesList[hole]) + ': ')
            while True:  # Makes sure the user enters a valid input
                try:
                    playerInput = int(input())
                except ValueError:
                    print('Please enter an integer.')
                else:
                    break
            playerList[player][1].append(playerInput)  # Adds the input to the appropriate player's score in the player
            # list
        if holesPlayed < holes - 1:  # Makes the live scoreboard not be printed on the last hole
            sortedList = sort_players(playerList)
            make_live_scoreboard(sortedList)
            holesPlayed += 1
    print_bar()
    print('The game is finished!')
    input('Press enter to see who won! ')
    return playerList

def make_final_list(players, playerList):  # This function creates a final list once the game has finished
    finalList = []
    for player in range(0, players):
        player = (playerList[player][0], sum(playerList[player][1]))  # Sums the list of scores so it can be displayed
        finalList.append(player)
    return finalList

def make_scoreboard(sortedList):  # This function makes the final scoreboard displayed at the end of the game
    places = ['1st', '2nd', '3rd', '4th']  # List of places to be entered in the live scoreboard
    print_gap()
    print('Scoreboard:')
    print_bar()
    for player in range(0, len(sortedList)):  # Loop that creates scoreboard depending on number of players
        print(sortedList[player][0], 'came in', places[player], 'place with a score of', str(sortedList[player][1]) +
              '!')
    print_bar()
    input('Press enter to continue. ')

def play_again():  # This function asks the user if it would like to play again
    print_gap()
    check = True
    again = True
    while check:  # Will continue to check if the user enters a value other than 1 or 2
        print('Would you like to play again?')
        print('Press (1) for yes or (2) for no: ')
        while True:
            try:  # Makes sure user input is valid
                againKey = int(input())
            except ValueError:
                print('Please enter 1 or 2.')
            else:
                break
        if againKey == 1:
            print_gap()
            again = True
            check = False
        elif againKey == 2:
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
        holeCount = get_holes()
        holesList = make_holes_list(holeCount)
        while holeCount > 9 or holeCount < 1:  # Checks hole count if user entered a value that was out of range
            holeCount = check_hole_count(holeCount)
        playerCount = get_player_count()
        while playerCount > 4 or playerCount < 1:  # Checks player count if user entered a value that was out of range
            playerCount = check_player_count(playerCount)
        playerNames = get_player_names(playerCount)
        playerList = make_player_list(playerCount, playerNames)
        playerList = get_scores(holeCount, playerCount, playerList, holesList)
        finalList = make_final_list(playerCount, playerList)
        sortedList = sort_players(finalList)
        make_scoreboard(sortedList)
        playing = play_again()
    print_outro()

# CALL TO MAIN #
main()
