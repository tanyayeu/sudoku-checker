# SUDOKU
# Tanya Yeu (yeut@oregonstate.edu)

# Description: Checks that number is between 1-9 and returns True/False
# Parameters: an integer
def isValid(num):
    if num > 0 and num <= 9:
        return True
    else:
        return False

# Description: Checks the format of the solution for a 9x9 answer and returns true/false
# Parameters: 2d 9x9 array
def checkFormat(solution):
    if(len(solution) != 9):
        return False
    for row in solution:
        if(len(row) != 9):
            return False
    return True

# Parameter: array of integers
# Description: checks that the numbers are valid and there are no duplicates
def isValidRow(arr):
    input = [0 for y in range(10)]
    for x in range(len(arr)):
        if(isValid(arr[x]) == False or input[arr[x]] ==1): #if the number is not in 1-9, return
            return False
        elif input[arr[x]] != 1:
            input[arr[x]] = 1
        #elif input[arr[x]] == 1:
         #   return False
    return True

# Parameter: Takes a 2d array (the board) as the answer
# Description: Will check that it is a 9x9 solution, then checks rows, columns, and subgrids

def checkAnswer(answer):
    if(checkFormat(answer) == False):
        print("The answer is not formatted correctly. Please verify this is a 9x9 solution")
        return -1
    #check each row in the answer that there are no duplicates
    for row in answer:
        if(isValidRow(row) == False):
             print("Not solved, try again!!")
             return -1    
    #check columns
    for column in range(len(answer[0])):
        placed = [0 for z in range(10)]
        for i in range(0,9):
            if(isValid(answer[i][0]) and placed[answer[i][0]] != 1):
                placed[answer[i][0]] = 1
            elif placed[answer[i][0]] ==1:
                print("Not solved, try again!!")
                return -1
    #check subgrids
    for row in range(2, 9, 3):
        indexCol = 0
        #loop through 3x
        for x in range(0,3):
            indexCol +=3
            placed = [0 for p in range(10)]
            for subRow in range(row-2, row+1):
                for col in range(indexCol-3, indexCol):
                    num = answer[subRow][col]
                    if(isValid(num) and placed[num] != 1):
                        placed[num] = 1
                    else: 
                        print("Not solved, try again!!")
                        return -1
    print("SOLVED!!")
    return 1

# Parameter: takes 2d array
# Prints the board with sudoku borders
def printBoard(board):
    topBorder = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    bottomBorder = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"
    middleLine = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    middleGridLine = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    gridLine = "║"
    spaceLine = "│"
    print(topBorder)
    for rows in range(0,len(board)):
        print(gridLine,end='')
        for col in range(0,len(board[0])):
            num = board[rows][col]
            if(num != 0):
                print(' ',num, end = '')
            elif(num == 0):
                print("   ", end='')
            #print(spaceLine, end='')
            if((col+1) %3 == 0):
                print(gridLine,end='')
            else: print(spaceLine,end='')
        print("\n", end='')
        if(rows == 8):
            print(bottomBorder)
        elif((rows + 1) % 3 == 0):
            print(middleLine)
        else: print(middleGridLine)

#Prints the instructions for the game
def printInstructions():
    print("Let's play to SUDOKU!")
    print("Given the following 9x9 grid, fill out the blanks with numbers 1-9.")
    print("Each row, column, and 3x3 grid cannot have repeating numbers.")

# Parameters: n for number of elements in each row
# Gets the input and puts it into a 2d array
def getInput(n):
    answer = [[0 for y in range(1)] for z in range(9)]
    print("Enter each number in row with a space between and hit enter at the end of the row")
    for x in range(0,n):
        print("Row",x+1)
        row = list(map(int,input("Enter the row: ").strip().split()))[:n]
        answer[x] = row
    return answer

#Predefined intermediate board            
board = [[0,2,0,6,0,8,0,0,5],
            [5,8,0,0,0,9,7,0,0],
            [0,0,0,0,4,0,0,0,0],
            [3,7,0,0,6,0,5,0,0],
            [6,0,0,0,8,0,0,0,4],
            [0,0,8,0,0,0,0,1,3],
            [0,0,0,0,2,0,0,0,0],
            [0,1,9,8,0,0,0,3,6],
            [7,0,0,3,0,6,0,9,0]]            

#Gets the column number and row number and inserts it onto the board and reprints it
def insertNum(board):
    row = int(input("Enter row number:"))
    while(isValid(row) == False):
        print("Not a valid number.")
        row = int(input("Enter row number:"))
    col = int(input("Enter column number:"))
    while(isValid(col) == False):
        print("Not a valid number.")
        col = int(input("Enter column number:"))
    num = int(input("Enter number:"))
    while(isValid(num) == False):
        print("Not a valid number.")
        num = int(input("Enter number:"))
    row = row -1
    col = col - 1
    board[row][col] = num
    printBoard(board)
    return board

#Presents the options
def selectChoice():
    print("Select 1 of the following choices:")
    x = int(input("1. Insert Number\n"
                        "2. Check answers\n"
                        "3. Quit\n"
                        "Choice: "))
    return x

#Driver code
def playGame(board):
    printInstructions()
    printBoard(board)
    choice = selectChoice()
    while(choice != 3):
        if(choice == 1):
            board = insertNum(board)
        if(choice == 2):
            x = checkAnswer(board)
            if x == 1: return
        choice = selectChoice()
    if(choice == 3):
        return

playGame(board)

"""
ANSWER:
1 2 3 6 7 8 9 4 5
5 8 4 2 3 9 7 6 1
9 6 7 1 4 5 3 2 8
3 7 2 4 6 1 5 8 9
6 9 1 5 8 3 2 7 4
4 5 8 7 9 2 6 1 3
8 3 6 9 2 4 1 5 7
2 1 9 8 5 7 4 3 6
7 4 5 3 1 6 8 9 2
"""