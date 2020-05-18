import random
import copy
import os

boardSize = 5 #default
print("Custom Board size?")
userinp = input ('y or n?')
if userinp == 'y':
    boardSize = int(input("Enter the size of the board. (Must be an intiger)"))
    if boardSize<=0:
        print("Invalid size specified. Will proceed with deafult.")
        boardSize = 5


maxno=2048 #default
print("Custom Winning Number?")
userinpn = input('y or n?')
if userinpn == 'y':
    maxno = int (input ("What should be the number to win? (Will be rounded to the nearest upper power of input)"))

#I will check if the winning number is actually achievable 
a=0
while(2**a<maxno):
    a+=1
    winno=2**a
#if the maximum possible number in the board is less, that will be the new winning number
winno = min( winno, 2**(boardSize**2) )

#Informing the player about his goals, which might have changed because of invlid inputs
print ('Reach ' + str(winno) + ' to win. All the best!')
print ("If you wanna exit midway, press 'q'")
#I will make sure that the grid does not distort at higher numbers by giving it white spaces 
#to the right, so that all the numbers are alligned properly in columns and the maximum no of
#whitespaces will match the space required to display the biggest number without misallignment.
numspaces = len(str(winno))

def display():
    for row in board:
        currow = ''
        for element in row:
            currow += str(element) + (' ' * (numspaces - len(str(element))))  + ' '
            #making a string out of the current row, so that it can be displayed withou bracket
        print(currow)

def mergeOneRowL(row):
    #Moving everything to the left, i.e occupying zeroes   
    for j in range(boardSize):
        for i in range(boardSize-1, 0, -1):
            #Check if there is empty space to move towards
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0 

    for i in range(boardSize-1):
    #If same values, double them
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0

    #however, sometimes, we may get the row as 4 0 4 0 using the above doubling snippet of code
    #so, we will again, kill the zeroes on the left
    for i in range(boardSize-1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    
    return row  

def mergeleft(currentboard):
    #Merge every row in the board towards left
    for i in range(boardSize):
        currentboard[i] = mergeOneRowL(currentboard[i])

    return currentboard

def reverse(row):
    new = []
    for i in range(boardSize-1,-1,-1):
        new.append(row[i])
    return new

#Since the code is huge, to move right, we will mirror the board, move it to the left and mirror again to get the proper board
def mergeright(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

#We will take it and take the transpose so that now we can deal with the board 
# with the horizontol movement commands, and then take the transpose to get it back
def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = int(0)
                temp=currentBoard[i][j]
                currentBoard[i][j]=currentBoard[j][i]
                currentBoard[j][i]=temp
    return currentBoard

def mergedown(currentBoard):
    currentBoard=transpose(currentBoard)
    currentBoard=mergeright(currentBoard)
    currentBoard=transpose(currentBoard)

    return currentBoard


def mergeup(currentBoard):
    currentBoard=transpose(currentBoard)
    currentBoard=mergeleft(currentBoard)
    currentBoard=transpose(currentBoard)

    return currentBoard 

#Lets pick up a two or a four using the random function, where one out of 10 times, a 4 is picked up
def picknewvalue():
    if random.randint(1,10)==1:
        return 4
    else:
        return 2

#Now, lets make the game board    
board=[]

for i in range(boardSize):
    row=[]
    for j in range(boardSize):
        row.append(0)
    board.append(row)


#Pick up the values of the to be filled initially 
done = False
while not done:
    rowNum = random.randint(0, boardSize-1)
    colNum = random.randint(0, boardSize-1)
    
    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = picknewvalue()
        done = True

#To spawn a random tile every single time a valid move is played
def addnew():
    rowNum = random.randint(0,boardSize-1)
    colNum = random.randint(0,boardSize-1)

    #keep picking till the spot is empty
    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0,boardSize-1)
        colNum = random.randint(0,boardSize-1)

    board[rowNum][colNum] = picknewvalue()

#Function to sweep board if the winning number is present
def won():
    for row in board:
        if winno in row:
            return True
    return False

#To check if there are no more playable moves in either of the four directions, so 
# that we can check if the game is lost
def lost():
    tempboard1=copy.deepcopy(board)
    tempboard2=copy.deepcopy(board)

    tempboard1=mergedown(tempboard1)
    if tempboard1 == tempboard2:
        tempboard1 = mergeleft(tempboard1)
        if tempboard1 == tempboard2:
            tempboard1 = mergeright(tempboard1)
            if tempboard1 == tempboard2:
                tempboard1 = mergeup(tempboard1)
                if tempboard1 == tempboard2:
                    return True
    return False

#Lets show the player the board
display()


gameOver = False #Because its just getting started

#ErrorHandling
if boardSize == 1:
    print('The game is already won. Lol. ')
    gameOver = True

while not gameOver:
    move = input ("Which way to move?")

    #Clearinf the board on every move
    os.system('cls')
    
    validInput = True

    #Thank you :) for explaining the difference between the normal copy and deepcopy
    tempboard01 = copy.deepcopy(board)

    if move == 'd':
        board = mergeright(board)

    elif move == 'a':
        board = mergeleft(board)

    elif move == 'w':
        board = mergeup(board)

    elif move == 's':
        board = mergedown(board)

    elif move == 'q':
        #Exit function, if you wanna give up midway.
        break

    else:
        validInput=False 
    
    if not validInput:
        print("Your input is not valid, please try again")

    else:
        
        #Because if you arent moving any tile, you dont deserve a new one :P
        if board == tempboard01:
            print("this move was invalid")
        
        else:
            if won():
                display()
                print("Congratulations! You Won.")
                gameOver = True    

            else:
                #since we have already movedm we will spawn a random tile too
                addnew()
                display()

                if lost():
                    print("No more moves left. So, you lost.")
                    gameOver = True