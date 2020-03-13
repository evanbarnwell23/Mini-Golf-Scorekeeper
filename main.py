# Evan Barnwell
# Integration Project
# Dorm MiniGolf Scorekeeper
# This program keeps score of a game of Dorm MiniGolf.
# The program supports up to 9 holes and up to 4 players.
# The program prints player scores at the end of the game.


def gap():
    print('.')
    print('.')
    print('.')


def bar():
    print('------------------------------------------------------------------------')


def intro():
    print("Welcome to Dorm MiniGolf Scorekeeper!")
    input('Press enter to begin: ')
    gap()


def getHoles():
    print('Please enter the number of holes you would like to play: ')
    for hole in range(1, 10):
        print('(' + str(hole) + ')', str(hole), end='  ')
    while True:
        try:
            holes = int(input())
        except ValueError:
            gap()
            print('Please enter a number between 1 and 9: ')
        else:
            break
    return holes


def make_holesList(holes):
    holesList = list(range(1, holes + 1))
    return holesList


def check_holeCount(holes):
    check = True
    while check:
        gap()
        print('Please enter a number between 1 and 9: ')
        for hole in range(1, 10):
            print('(' + str(hole) + ')', str(hole), end='  ')
        while True:
            try:
                holes = int(input())
            except ValueError:
                gap()
                print('Please enter a number between 1 and 9: ')
            else:
                check = False
                break
    return holes


def get_playerCount():
    gap()
    print('Please enter the number of players: ')
    for player in range(1, 5):
        print('(' + str(player) + ')', str(player), end='  ')
    while True:
        try:
            players = int(input())
        except ValueError:
            print('Please enter an integer between 1 and 4: ')
        else:
            break
    return players


def check_playerCount(players):
    check = True
    while check:
        gap()
        print('Please enter a number between 1 and 4: ')
        for player in range(1, 5):
            print('(' + str(player) + ')', str(player), end='  ')
        while True:
            try:
                players = int(input())
            except ValueError:
                gap()
                print('Please enter a number between 1 and 4: ')
            else:
                check = False
                break
    return players


def get_playerNames(players):
    gap()
    playerNames = []
    for player in range(1, players + 1):
        playerNames.append(input('Enter the name of Player ' + str(player) + ': '))
    return playerNames


def make_playerList(playerCount, playerNames):
    playerList = []
    for player in range(1, playerCount + 1):
        playerList.append([playerNames[player - 1], []])
    return playerList


def sortPlayers(playerList):
    sortedList = sorted(playerList, key=lambda tup: tup[1])
    return sortedList


def liveScoreboard(sortedList):
    places = ['1st', '2nd', '3rd', '4th']
    print('Scoreboard:')
    bar()
    for player in range(0, len(sortedList)):
        print(sortedList[player][0], 'is in', places[player], 'place with a score of', str(sum(sortedList[player][1])) +
              '!')
    bar()


def getScores(holes, players, playerList, holesList):
    holesPlayed = 0
    for hole in range(0, holes):
        gap()
        print('Hole', str(hole + 1) + ': ')
        bar()
        for player in range(0, players):
            print('Enter', playerList[player][0] + "'s score on hole", str(holesList[hole]) + ': ')
            while True:
                try:
                    playerInput = int(input())
                except ValueError:
                    print('Please enter an integer.')
                else:
                    break
            playerList[player][1].append(playerInput)
        if holesPlayed < holes - 1:
            sortedList = sortPlayers(playerList)
            liveScoreboard(sortedList)
            holesPlayed += 1
    bar()
    print('The game is finished!')
    input('Press enter to see who won! ')
    return playerList


def make_finalList(players, playerList):
    finalList = []
    for player in range(0, players):
        player = (playerList[player][0], sum(playerList[player][1]))
        finalList.append(player)
    return finalList


def makeScoreboard(sortedList):
    places = ['1st', '2nd', '3rd', '4th']
    gap()
    print('Scoreboard:')
    bar()
    for player in range(0, len(sortedList)):
        print(sortedList[player][0], 'came in', places[player], 'place with a score of', str(sortedList[player][1]) +
              '!')
    bar()
    input('Press enter to continue. ')


def playAgain():
    gap()
    check = True
    again = True
    while check:
        print('Would you like to play again?')
        print('Press (1) for yes or (2) for no: ')
        while True:
            try:
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
    return again


def outro():
    gap()
    print('Goodbye!')


def main():
    intro()
    holeCount = getHoles()
    holesList = make_holesList(holeCount)
    if holeCount > 9 or holeCount < 1:
        holeCount = check_holeCount(holeCount)
    playerCount = get_playerCount()
    if playerCount > 4 or playerCount < 1:
        playerCount = check_playerCount(playerCount)
    playerNames = get_playerNames(playerCount)
    playerList = make_playerList(playerCount, playerNames)
    playerList = getScores(holeCount, playerCount, playerList, holesList)
    finalList = make_finalList(playerCount, playerList)
    sortedList = sortPlayers(finalList)
    makeScoreboard(sortedList)
    again = playAgain()
    if not again:
        outro()
    else:
        main()


# CALL TO MAIN #
main()
