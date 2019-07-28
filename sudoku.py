from tkinter import *

# Sudoku Solver with GUI
# By Ryan Rasi
# http://ryanrasi.com
# https://github.com/RyanRasi

# Global Arrays

RowOne = []
RowTwo = [] 
RowThr = [] 
RowFou = [] 
RowFiv = [] 
RowSix = [] 
RowSev = [] 
RowEig = [] 
RowNin = [] 

board = []

solved = []

# Menu Choice

print("Would you like to use the default board or import your own to solve? \n 1. Default \n 2. Import")
menu = int(input())

if (menu == 1):
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    print("Board set")

if (menu == 2):

    board = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []    
    ]

    RowOne = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 1\n").split(" ")))

    RowTwo = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 2\n").split(" ")))

    RowThr = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 3\n").split(" ")))

    RowFou = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 4\n").split(" ")))

    RowFiv = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 5\n").split(" ")))

    RowSix = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 6\n").split(" ")))

    RowSev = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 7\n").split(" ")))

    RowEig = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 8\n").split(" ")))

    RowNin = list(map(int,input("Please enter each full row of the sudoku board with blank numebrs indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 9\n").split(" ")))

    board[0] = RowOne
    board[1] = RowTwo
    board[2] = RowThr
    board[3] = RowFou
    board[4] = RowFiv
    board[5] = RowSix
    board[6] = RowSev
    board[7] = RowEig
    board[8] = RowNin    


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                solved.append((bo[i][j]))
                print(bo[i][j])
            else:
                solved.append(str(bo[i][j]))
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
# Prints the pre-solved board
print("Pre-solved Board")
print_board(board) 
print("_______________________\n_______________________\n")
# Solves the board
solve(board)
# Prints the solved board
print("Solved Board")
print_board(board)
print("_______________________\n_______________________\n")
# Print all of the solved board - debug
# print(*solved, sep = "\n") 
# print("_______________________\n_______________________\n")

# Prints the second value that is solved
print(solved[1])

# Start of GUI ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

win = Tk ()

win.title("Sudoku Solved!")

win.geometry("475x470")
win.resizable(0, 0)

w = Canvas(win, width=475, height=470)
# w.create_rectangle(50, 0, 100, 50, fill="white", outline = 'black')


bOne = 1
for x in range(3):

# First Row of Boxes

        w.create_rectangle(5, (50 * bOne) - 45, 55, (50 * bOne) + 5, fill="white", outline = 'black')
        w.create_rectangle(55, (50 * bOne) - 45, 105, (50 * bOne) + 5, fill="white", outline = 'black')
        w.create_rectangle(105, (50 * bOne) - 45, 160, (50 * bOne) + 5, fill="white", outline = 'black')

        w.create_rectangle(165, (50 * bOne) - 45, 215, (50 * bOne) + 5, fill="white", outline = 'black')
        w.create_rectangle(215, (50 * bOne) - 45, 265, (50 * bOne) + 5, fill="white", outline = 'black')
        w.create_rectangle(265, (50 * bOne) - 45, 315, (50 * bOne) + 5, fill="white", outline = 'black')

        w.create_rectangle(320, (50 * bOne) - 45, 370, (50 * bOne) + 5, fill="white", outline = 'black')
        w.create_rectangle(370, (50 * bOne) - 45, 420, (50 * bOne) + 5, fill="white", outline = 'black')
        w.create_rectangle(420, (50 * bOne) - 45, 470, (50 * bOne) + 5, fill="white", outline = 'black')

# Second Row of Boxes

        w.create_rectangle(5, (50 * bOne) + 110, 55, (50 * bOne) + 160, fill="white", outline = 'black')
        w.create_rectangle(55, (50 * bOne) + 110, 105, (50 * bOne) + 160, fill="white", outline = 'black')
        w.create_rectangle(105, (50 * bOne) + 110, 160, (50 * bOne) + 160, fill="white", outline = 'black')

        w.create_rectangle(165, (50 * bOne) + 110, 215, (50 * bOne) + 160, fill="white", outline = 'black')
        w.create_rectangle(215, (50 * bOne) + 110, 265, (50 * bOne) + 160, fill="white", outline = 'black')
        w.create_rectangle(265, (50 * bOne) + 110, 315, (50 * bOne) + 160, fill="white", outline = 'black')

        w.create_rectangle(320, (50 * bOne) + 110, 370, (50 * bOne) + 160, fill="white", outline = 'black')
        w.create_rectangle(370, (50 * bOne) + 110, 420, (50 * bOne) + 160, fill="white", outline = 'black')
        w.create_rectangle(420, (50 * bOne) + 110, 470, (50 * bOne) + 160, fill="white", outline = 'black')

# Third Row of Boxes

        w.create_rectangle(5, (50 * bOne) + 265, 55, (50 * bOne) + 315, fill="white", outline = 'black')
        w.create_rectangle(55, (50 * bOne) + 265, 105, (50 * bOne) + 315, fill="white", outline = 'black')
        w.create_rectangle(105, (50 * bOne) + 265, 160, (50 * bOne) + 315, fill="white", outline = 'black')

        w.create_rectangle(165, (50 * bOne) + 265, 215, (50 * bOne) + 315, fill="white", outline = 'black')
        w.create_rectangle(215, (50 * bOne) + 265, 265, (50 * bOne) + 315, fill="white", outline = 'black')
        w.create_rectangle(265, (50 * bOne) + 265, 315, (50 * bOne) + 315, fill="white", outline = 'black')

        w.create_rectangle(320, (50 * bOne) + 265, 370, (50 * bOne) + 315, fill="white", outline = 'black')
        w.create_rectangle(370, (50 * bOne) + 265, 420, (50 * bOne) + 315, fill="white", outline = 'black')
        w.create_rectangle(420, (50 * bOne) + 265, 470, (50 * bOne) + 315, fill="white", outline = 'black')

        bOne += 1

# Labels
ROne = 1
for x in range(3):
        mylabel = w.create_text((ROne * 50) - 20, 30, text=solved[ROne - 1])
        mylabel = w.create_text((ROne * 50) + 140, 30, text=solved[ROne + 2])
        mylabel = w.create_text((ROne * 50) + 295, 30, text=solved[ROne + 5])

        ROne += 1

RTwo = 1
for x in range(3):
        mylabel = w.create_text((RTwo * 50) - 20, 80, text=solved[RTwo + 8])
        mylabel = w.create_text((RTwo * 50) + 140, 80, text=solved[RTwo + 11])
        mylabel = w.create_text((RTwo * 50) + 295, 80, text=solved[RTwo + 14])

        RTwo += 1

RThree = 1
for x in range(3):
        mylabel = w.create_text((RThree * 50) - 20, 130, text=solved[RThree + 17])
        mylabel = w.create_text((RThree * 50) + 140, 130, text=solved[RThree + 20])
        mylabel = w.create_text((RThree * 50) + 295, 130, text=solved[RThree + 23])

        RThree += 1

RFour = 1
for x in range(3):
        mylabel = w.create_text((RFour * 50) - 20, 185, text=solved[RFour + 26])
        mylabel = w.create_text((RFour * 50) + 140, 185, text=solved[RFour + 29])
        mylabel = w.create_text((RFour * 50) + 295, 185, text=solved[RFour + 32])

        RFour += 1

RFive = 1
for x in range(3):
        mylabel = w.create_text((RFive * 50) - 20, 235, text=solved[RFive + 35])
        mylabel = w.create_text((RFive * 50) + 140, 235, text=solved[RFive + 38])
        mylabel = w.create_text((RFive * 50) + 295, 235, text=solved[RFive + 41])

        RFive += 1

RSix = 1
for x in range(3):
        mylabel = w.create_text((RSix * 50) - 20, 285, text=solved[RSix + 44])
        mylabel = w.create_text((RSix * 50) + 140, 285, text=solved[RSix + 47])
        mylabel = w.create_text((RSix * 50) + 295, 285, text=solved[RSix + 50])

        RSix += 1

RSeven = 1
for x in range(3):
        mylabel = w.create_text((RSeven * 50) - 20, 340, text=solved[RSeven + 53])
        mylabel = w.create_text((RSeven * 50) + 140, 340, text=solved[RSeven + 56])
        mylabel = w.create_text((RSeven * 50) + 295, 340, text=solved[RSeven + 59])

        RSeven += 1

REight = 1
for x in range(3):
        mylabel = w.create_text((REight * 50) - 20, 390, text=solved[REight + 62])
        mylabel = w.create_text((REight * 50) + 140, 390, text=solved[REight + 65])
        mylabel = w.create_text((REight * 50) + 295, 390, text=solved[REight + 68])

        REight += 1

RNine = 1
for x in range(3):
        mylabel = w.create_text((RNine * 50) - 20, 440, text=solved[RNine + 71])
        mylabel = w.create_text((RNine * 50) + 140, 440, text=solved[RNine + 74])
        mylabel = w.create_text((RNine * 50) + 295, 440, text=solved[RNine + 77])

        RNine += 1
#solve(board)
#print_board(board)

w.pack()

win.mainloop ()
