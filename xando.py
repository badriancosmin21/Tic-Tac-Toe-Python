
import random
import time

compChoice = None
gameType = None
newGame = None  
gameWon = 0
scoreX = 0
scoreO = 0
aux = 0
compTurn = 0

def printList(arr):
    for row in arr:
        print(" ".join(row))

#---CHECK GAME TYPE (PvP OR VS COM)
while True:
    try:
        gameType = input("Would you like to play against COMPUTER or Player vs Player? (COM/PvP): ")
    except ValueError:
        print("Please pick COM or PvP")
    if gameType not in ('COM','PvP'):
        print("Please pick COM or PvP")
    else:
        break


while True:

    #---CHECK FOR GAME RESTART
    if newGame == 'N':
        break
    elif newGame == 'Y' or aux == 0:
        arr = [['_','_','_'],
               ['_','_','_'],
               ['_','_','_']]
        availableMoves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        gameWon = 0
        newGame = None
        for row in arr:
            print (" ".join(row))

        #---PLAY AS X OR O
        while True:
            try:
                choice = input("What do you want to play as?(X/O): ")
            except ValueError:
                print("Please pick X or O")
                continue
            if choice not in ('X','O'):
                print("Please pick X or O")
                continue
            else:
                break
        if choice == 'X':
            compChoice = 'O'
        else:
            compChoice = 'X'
    aux = 1
    
    #---PLAYER INPUT
    while True:
        row, col = input("Which position do you want to fill? " + choice + " :").split()
        row = int(row)
        col = int(col) 
    
        if arr[row][col] == '_':
            arr[row][col] = choice
            availableMoves.remove([row, col])
            if gameType == "COM":
                printList(arr)
            break
        else:
            print("Unavailable Position! Pick again")
            continue
    print("\n\n")

    #---COMPUTER INPUT
    if gameType == 'COM':
        for i in range (0,len(arr)):
            if arr[i][0] == arr[i][1] in (compChoice, choice) and arr[i][2] == '_':
                arr[i][2] = compChoice
                compTurn = 1
                availableMoves.remove([i, 2])
                break
            elif arr[i][1] == arr[i][2] in (compChoice, choice) and arr[i][0] == '_':
                arr[i][0] = compChoice
                compTurn = 1
                break
            elif arr[i][0] == arr[i][2] in (compChoice, choice) and arr[i][1] == '_':
                arr[i][1] = compChoice
                compTurn = 1
                availableMoves.remove([i, 1])
                break
            elif arr[0][i] == arr[1][i] in (compChoice, choice) and arr[2][i] == '_':
                arr[2][i] = compChoice
                compTurn = 1
                availableMoves.remove([2, i])
                break
            elif arr[1][i] == arr[2][i] in (compChoice, choice) and arr[0][i] == '_':
                arr[0][i] = compChoice
                compTurn = 1
                availableMoves.remove([0, i])
                break
            elif arr[0][i] == arr[2][i] in (compChoice, choice) and arr[1][i] == '_':
                arr[1][i] = compChoice
                compTurn = 1
                availableMoves.remove([1, i])
                break
        if compTurn == 0:
            if arr[0][0] == arr[1][1] in (compChoice, choice) and arr[2][2] == '_':
                arr[2][2] = compChoice
                availableMoves.remove([2, 2])
                break
            elif arr[0][0] == arr[2][2] in (compChoice, choice) and arr[1][1] == '_':
                arr[1][1] = compChoice
                availableMoves.remove([1, 1])
                break
            elif arr[1][1] == arr[2][2] in (compChoice, choice) and arr[0][0] == '_':
                arr[0][0] = compChoice
                availableMoves.remove([0, 0])
                break
            elif arr[0][2] == arr[1][1] in (compChoice, choice) and arr[2][0] == '_':
                arr[2][0] = compChoice
                availableMoves.remove([2, 0])
                break
            elif arr[0][2] == arr[2][0] in (compChoice, choice) and arr[1][1] == '_':
                arr[1][1] = compChoice
                availableMoves.remove([1, 1])
                break
            elif arr[1][1] == arr[2][0] in (compChoice, choice) and arr[0][2] == '_':
                arr[0][2] = compChoice
                availableMoves.remove([0, 2])
                break
            else:
                rand = random.randint(0,len(availableMoves)-1)
                arr[availableMoves[rand][0]][availableMoves[rand][1]] = compChoice 
                availableMoves.pop(rand)

    #---CHECK ROWS FOR WINNER
    for i in range (0,len(arr)):
        if arr[i][0] == arr[i][1] == arr[i][2] in ('X', 'O'):
            if arr[i][0] == 'X':
                scoreX += 1
            else:
                scoreO += 1
            print(arr[i][0] + " has won")
            gameWon = 1
            break

        elif arr[0][i] == arr[1][i] == arr[2][i] in ('X', 'O'):
            if arr[0][i] == 'X':
                scoreX += 1
            else:
                scoreO += 1
            print(arr[0][i] + " has won")
            gameWon = 1
            break

    if arr[0][0] == arr[1][1] == arr[2][2] in ('X', 'O'): 
        if arr[0][0] == 'X':
            scoreX += 1
        else:
            scoreO += 1
        print(arr[0][0] + " has won")
        gameWon = 1

    if arr[0][2] == arr[1][1] == arr[2][0] in ('X', 'O'):
        if arr[0][2] == 'X':
            scoreX += 1
        else:
            scoreO += 1
        print(arr[0][2] + " has won")
        gameWon = 1
    if gameType == "COM":
        time.sleep(1)
        printList(arr)

    #---PRINT WINNER
    if gameWon == 1:
        print('X score: ' + str(scoreX) + '   / O score: ' + str(scoreO))

        #-GAME RESTART
        while(True):
            try:
                newGame = input("Do you want to start again? (Y/N): ")
            except ValueError:
                print("Please pick Y(Yes) or N(No)")
                continue
            if newGame not in ('Y','N'):
                print("Please pick Y(Yes) or N(No)")
                continue
            else:
                break

    #---DRAW SITUATION
    if len(availableMoves) == 0:
        print("It's a draw!")
        while(True):
            try:
                newGame = input("Do you want to start again? (Y/N): ")
            except ValueError:
                print("Please pick Y(Yes) or N(No)")
                continue
            if newGame not in ('Y','N'):
                print("Please pick Y(Yes) or N(No)")
                continue
            else:
                break

    #---CHANGE CHOICE FOR PvP
    if gameType == 'PvP':            
        if choice == 'X':
            choice = 'O'
        else:
            choice ='X'
    
    compTurn = 0
