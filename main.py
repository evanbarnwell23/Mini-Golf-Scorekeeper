# Evan Barnwell
# Integration Project
# MiniGolf Scorekeeper
# This program keeps score of a game of MiniGolf.
# The program supports up to 9 holes and up to 4 players.
# The program prints player scores at the end of the game.


def gap():  # This function prints a 'gap' to separate parts of the scorekeeper for readability
    print('.')
    print('.')
    print('.')


def bar():  # This function prints a 'bar' to separate parts of the scorekeeper for readability
    print('------------------------------------------------------------------------')


def intro():  # This function prints the introduction the the scorekeeper
    print("Welcome to Dorm MiniGolf Scorekeeper!")
    input('Press enter to begin: ')
    gap()


def getHoles():  # This function gets the number of holes the user would like to score
    print('Please enter the number of holes you would like to play: ')
    for hole in range(1, 10):  # Prints choices for number of holes in multiple choice fashion
        print('(' + str(hole) + ')', str(hole), end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            holes = int(input())
        except ValueError:
            gap()
            print('Please enter a number between 1 and 9: ')
        else:
            break
    return holes  # Returns an amount of holes


def make_holesList(holes):  # This function makes the holes into a list
    holesList = list(range(1, holes + 1))
    return holesList


def check_holeCount(holes):  # This function ensures the user entered a valid number of holes
    gap()
    print('Please enter a number between 1 and 9: ')
    for hole in range(1, 10):  # Prints choices for number of holes in multiple choice fashion
        print('(' + str(hole) + ')', str(hole), end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            holes = int(input())
        except ValueError:
            gap()
            print('Please enter a number between 1 and 9: ')
        else:
            break
    return holes  # Returns an amount of holes


def get_playerCount():  # This function gets the number of players the user would like to score
    gap()
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


def check_playerCount(players):  # This function ensures the user entered a valid number of players
    gap()
    print('Please enter a number between 1 and 4: ')
    for player in range(1, 5):  # Prints choices for number of holes in multiple choice fashion
        print('(' + str(player) + ')', str(player), end='  ')
    while True:  # This ensures the user inputs an integer
        try:
            players = int(input())
        except ValueError:
            gap()
            print('Please enter a number between 1 and 4: ')
        else:
            break
    return players  # Returns an amount of players


def get_playerNames(players):  # This function gets the names of the players
    gap()
    playerNames = []  # List that player names are stored in
    for player in range(1, players + 1):  # Loop to get player names base on number of players being scored
        playerNames.append(input('Enter the name of Player ' + str(player) + ': '))
    return playerNames  # Returns the list of player names


def make_playerList(playerCount, playerNames):  # This function creates a list of the players
    playerList = []
    for player in range(1, playerCount + 1):  # Loop creating players as elements of the list
        playerList.append([playerNames[player - 1], []])  # Each player/element of the list is a tuple
    return playerList  # Returns the list of players


def sortPlayers(playerList):  # This function sorts players based on their score (second element of the tuple)
    sortedList = sorted(playerList, key=lambda tup: tup[1])  # Sort taken from
    # https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    return sortedList  # Returns the player list sorted


def liveScoreboard(sortedList):  # This function prints a live scoreboard while the game is running
    places = ['1st', '2nd', '3rd', '4th']  # List of places to be entered in the live scoreboard
    print('Scoreboard:')
    bar()
    for player in range(0, len(sortedList)):  # Loop that creates scoreboard depending on number of players
        print(sortedList[player][0], 'is in', places[player], 'place with a score of', str(sum(sortedList[player][1])) +
              '!')
    bar()


def getScores(holes, players, playerList, holesList):  # This function gets player scores
    holesPlayed = 0
    for hole in range(0, holes):  # Loop for number of holes
        gap()
        print('Hole', str(hole + 1) + ': ')
        bar()
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
            sortedList = sortPlayers(playerList)
            liveScoreboard(sortedList)
            holesPlayed += 1
    bar()
    print('The game is finished!')
    input('Press enter to see who won! ')
    return playerList


def make_finalList(players, playerList):  # This function creates a final list once the game has finished
    finalList = []
    for player in range(0, players):
        player = (playerList[player][0], sum(playerList[player][1]))  # Sums the list of scores so it can be displayed
        finalList.append(player)
    return finalList


def makeScoreboard(sortedList):  # This function makes the final scoreboard displayed at the end of the game
    places = ['1st', '2nd', '3rd', '4th']  # List of places to be entered in the live scoreboard
    gap()
    print('Scoreboard:')
    bar()
    for player in range(0, len(sortedList)):  # Loop that creates scoreboard depending on number of players
        print(sortedList[player][0], 'came in', places[player], 'place with a score of', str(sortedList[player][1]) +
              '!')
    bar()
    input('Press enter to continue. ')


def playAgain():  # This function asks the user if it would like to play again
    gap()
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
            gap()
            again = True
            check = False
        elif againKey == 2:
            again = False
            check = False
        else:
            check = True
    return again  # Returns boolean for whether or not the program will run again


def outro():  # This function prints the outro to the scorekeeper
    gap()
    print('Goodbye!')


def main():  # This is the main function
    intro()
    holeCount = getHoles()
    holesList = make_holesList(holeCount)
    while holeCount > 9 or holeCount < 1:  # Checks hole count if user entered a value that wasn't in the correct range
        holeCount = check_holeCount(holeCount)
    playerCount = get_playerCount()
    while playerCount > 4 or playerCount < 1:  # Checks player count if user entered a value that was out of range
        playerCount = check_playerCount(playerCount)
    playerNames = get_playerNames(playerCount)
    playerList = make_playerList(playerCount, playerNames)
    playerList = getScores(holeCount, playerCount, playerList, holesList)
    finalList = make_finalList(playerCount, playerList)
    sortedList = sortPlayers(finalList)
    makeScoreboard(sortedList)
    again = playAgain()
    if not again:  # Prints outro if user doesn't want to play again
        outro()
    else:  # Calls main if the user wants to play again
        main()


# CALL TO MAIN #
main()
