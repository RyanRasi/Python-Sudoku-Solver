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

#    RowOne = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 1\n").split(" ")))

#    RowTwo = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 2\n").split(" ")))

#    RowThr = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 3\n").split(" ")))

#    RowFou = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 4\n").split(" ")))

#    RowFiv = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 5\n").split(" ")))

#    RowSix = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 6\n").split(" ")))

#    RowSev = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 7\n").split(" ")))

#    RowEig = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 8\n").split(" ")))

#    RowNin = list(map(int,input("Please enter each full row of the sudoku board with blank numbers indicated by a 0 and each number seperated by a space.\ne.g \'7 8 0 4 0 0 1 2 0\' \nRow 9\n").split(" ")))

# Start of GUI ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    win = Tk ()

    win.title("Sudoku Entry!")

    win.geometry("475x515")
    win.resizable(0, 0)

    w = Canvas(win, width=475, height=515)
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------

    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4 = StringVar()
    e5 = StringVar()
    e6 = StringVar()
    e7 = StringVar()
    e8 = StringVar()
    e9 = StringVar()

    entry_box = Entry(win, textvariable = e1, width=2).place(x = 15, y = 17.5)
    entry_box = Entry(win, textvariable = e2, width=2).place(x = 65, y = 17.5)
    entry_box = Entry(win, textvariable = e3, width=2).place(x = 115, y = 17.5)
    entry_box = Entry(win, textvariable = e4, width=2).place(x = 170, y = 17.5)
    entry_box = Entry(win, textvariable = e5, width=2).place(x = 230, y = 17.5)
    entry_box = Entry(win, textvariable = e6, width=2).place(x = 280, y = 17.5)
    entry_box = Entry(win, textvariable = e7, width=2).place(x = 335, y = 17.5)
    entry_box = Entry(win, textvariable = e8, width=2).place(x = 385, y = 17.5)
    entry_box = Entry(win, textvariable = e9, width=2).place(x = 435, y = 17.5)

    e10 = StringVar()
    e11 = StringVar()
    e12 = StringVar()
    e13 = StringVar()
    e14 = StringVar()
    e15 = StringVar()
    e16 = StringVar()
    e17 = StringVar()
    e18 = StringVar()

    entry_box = Entry(win, textvariable = e10, width=2).place(x = 15, y = 67.5)
    entry_box = Entry(win, textvariable = e11, width=2).place(x = 65, y = 67.5)
    entry_box = Entry(win, textvariable = e12, width=2).place(x = 115, y = 67.5)
    entry_box = Entry(win, textvariable = e13, width=2).place(x = 170, y = 67.5)
    entry_box = Entry(win, textvariable = e14, width=2).place(x = 230, y = 67.5)
    entry_box = Entry(win, textvariable = e15, width=2).place(x = 280, y = 67.5)
    entry_box = Entry(win, textvariable = e16, width=2).place(x = 335, y = 67.5)
    entry_box = Entry(win, textvariable = e17, width=2).place(x = 385, y = 67.5)
    entry_box = Entry(win, textvariable = e18, width=2).place(x = 435, y = 67.5)

    e19 = StringVar()
    e20 = StringVar()
    e21 = StringVar()
    e22 = StringVar()
    e23 = StringVar()
    e24 = StringVar()
    e25 = StringVar()
    e26 = StringVar()
    e27 = StringVar()

    entry_box = Entry(win, textvariable = e19, width=2).place(x = 15, y = 117.5)
    entry_box = Entry(win, textvariable = e20, width=2).place(x = 65, y = 117.5)
    entry_box = Entry(win, textvariable = e21, width=2).place(x = 115, y = 117.5)
    entry_box = Entry(win, textvariable = e22, width=2).place(x = 170, y = 117.5)
    entry_box = Entry(win, textvariable = e23, width=2).place(x = 230, y = 117.5)
    entry_box = Entry(win, textvariable = e24, width=2).place(x = 280, y = 117.5)
    entry_box = Entry(win, textvariable = e25, width=2).place(x = 335, y = 117.5)
    entry_box = Entry(win, textvariable = e26, width=2).place(x = 385, y = 117.5)
    entry_box = Entry(win, textvariable = e27, width=2).place(x = 435, y = 117.5)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

    e28 = StringVar()
    e29 = StringVar()
    e30 = StringVar()
    e31 = StringVar()
    e32 = StringVar()
    e33 = StringVar()
    e34 = StringVar()
    e35 = StringVar()
    e36 = StringVar()

    entry_box = Entry(win, textvariable = e28, width=2).place(x = 15, y = 172.5)
    entry_box = Entry(win, textvariable = e29, width=2).place(x = 65, y = 172.5)
    entry_box = Entry(win, textvariable = e30, width=2).place(x = 115, y = 172.5)
    entry_box = Entry(win, textvariable = e31, width=2).place(x = 170, y = 172.5)
    entry_box = Entry(win, textvariable = e32, width=2).place(x = 230, y = 172.5)
    entry_box = Entry(win, textvariable = e33, width=2).place(x = 280, y = 172.5)
    entry_box = Entry(win, textvariable = e34, width=2).place(x = 335, y = 172.5)
    entry_box = Entry(win, textvariable = e35, width=2).place(x = 385, y = 172.5)
    entry_box = Entry(win, textvariable = e36, width=2).place(x = 435, y = 172.5)

    e37 = StringVar()
    e38 = StringVar()
    e39 = StringVar()
    e40 = StringVar()
    e41 = StringVar()
    e42 = StringVar()
    e43 = StringVar()
    e44 = StringVar()
    e45 = StringVar()

    entry_box = Entry(win, textvariable = e37, width=2).place(x = 15, y = 222.5)
    entry_box = Entry(win, textvariable = e38, width=2).place(x = 65, y = 222.5)
    entry_box = Entry(win, textvariable = e39, width=2).place(x = 115, y = 222.5)
    entry_box = Entry(win, textvariable = e40, width=2).place(x = 170, y = 222.5)
    entry_box = Entry(win, textvariable = e41, width=2).place(x = 230, y = 222.5)
    entry_box = Entry(win, textvariable = e42, width=2).place(x = 280, y = 222.5)
    entry_box = Entry(win, textvariable = e43, width=2).place(x = 335, y = 222.5)
    entry_box = Entry(win, textvariable = e44, width=2).place(x = 385, y = 222.5)
    entry_box = Entry(win, textvariable = e45, width=2).place(x = 435, y = 222.5)

    e46 = StringVar()
    e47 = StringVar()
    e48 = StringVar()
    e49 = StringVar()
    e50 = StringVar()
    e51 = StringVar()
    e52 = StringVar()
    e53 = StringVar()
    e54 = StringVar()

    entry_box = Entry(win, textvariable = e46, width=2).place(x = 15, y = 272.5)
    entry_box = Entry(win, textvariable = e47, width=2).place(x = 65, y = 272.5)
    entry_box = Entry(win, textvariable = e48, width=2).place(x = 115, y = 272.5)
    entry_box = Entry(win, textvariable = e49, width=2).place(x = 170, y = 272.5)
    entry_box = Entry(win, textvariable = e50, width=2).place(x = 230, y = 272.5)
    entry_box = Entry(win, textvariable = e51, width=2).place(x = 280, y = 272.5)
    entry_box = Entry(win, textvariable = e52, width=2).place(x = 335, y = 272.5)
    entry_box = Entry(win, textvariable = e53, width=2).place(x = 385, y = 272.5)
    entry_box = Entry(win, textvariable = e54, width=2).place(x = 435, y = 272.5)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

    e55 = StringVar()
    e56 = StringVar()
    e57 = StringVar()
    e58 = StringVar()
    e59 = StringVar()
    e60 = StringVar()
    e61 = StringVar()
    e62 = StringVar()
    e63 = StringVar()

    entry_box = Entry(win, textvariable = e55, width=2).place(x = 15, y = 327.5)
    entry_box = Entry(win, textvariable = e56, width=2).place(x = 65, y = 327.5)
    entry_box = Entry(win, textvariable = e57, width=2).place(x = 115, y = 327.5)
    entry_box = Entry(win, textvariable = e58, width=2).place(x = 170, y = 327.5)
    entry_box = Entry(win, textvariable = e59, width=2).place(x = 230, y = 327.5)
    entry_box = Entry(win, textvariable = e60, width=2).place(x = 280, y = 327.5)
    entry_box = Entry(win, textvariable = e61, width=2).place(x = 335, y = 327.5)
    entry_box = Entry(win, textvariable = e62, width=2).place(x = 385, y = 327.5)
    entry_box = Entry(win, textvariable = e63, width=2).place(x = 435, y = 327.5)

    e64 = StringVar()
    e65 = StringVar()
    e66 = StringVar()
    e67 = StringVar()
    e68 = StringVar()
    e69 = StringVar()
    e70 = StringVar()
    e71 = StringVar()
    e72 = StringVar()

    entry_box = Entry(win, textvariable = e64, width=2).place(x = 15, y = 377.5)
    entry_box = Entry(win, textvariable = e65, width=2).place(x = 65, y = 377.5)
    entry_box = Entry(win, textvariable = e66, width=2).place(x = 115, y = 377.5)
    entry_box = Entry(win, textvariable = e67, width=2).place(x = 170, y = 377.5)
    entry_box = Entry(win, textvariable = e68, width=2).place(x = 230, y = 377.5)
    entry_box = Entry(win, textvariable = e69, width=2).place(x = 280, y = 377.5)
    entry_box = Entry(win, textvariable = e70, width=2).place(x = 335, y = 377.5)
    entry_box = Entry(win, textvariable = e71, width=2).place(x = 385, y = 377.5)
    entry_box = Entry(win, textvariable = e72, width=2).place(x = 435, y = 377.5)

    e73 = StringVar()
    e74 = StringVar()
    e75 = StringVar()
    e76 = StringVar()
    e77 = StringVar()
    e78 = StringVar()
    e79 = StringVar()
    e80 = StringVar()
    e81 = StringVar()

    entry_box = Entry(win, textvariable = e73, width=2).place(x = 15, y = 427.5)
    entry_box = Entry(win, textvariable = e74, width=2).place(x = 65, y = 427.5)
    entry_box = Entry(win, textvariable = e75, width=2).place(x = 115, y = 427.5)
    entry_box = Entry(win, textvariable = e76, width=2).place(x = 170, y = 427.5)
    entry_box = Entry(win, textvariable = e77, width=2).place(x = 230, y = 427.5)
    entry_box = Entry(win, textvariable = e78, width=2).place(x = 280, y = 427.5)
    entry_box = Entry(win, textvariable = e79, width=2).place(x = 335, y = 427.5)
    entry_box = Entry(win, textvariable = e80, width=2).place(x = 385, y = 427.5)
    entry_box = Entry(win, textvariable = e81, width=2).place(x = 435, y = 427.5)

    mylabel = w.create_text(211.5, 475, text="Enter the available numbers with a 0 to indicate a blank number")
    mylabel = w.create_text(171.25, 497.5, text="Close the window when finished to see the solution")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

    w.pack()

    win.mainloop ()

    tempRow = ((str(e1.get())) + " " + (str(e2.get())) + " " + (str(e3.get())) + " " + (str(e4.get())) + " " + (str(e5.get())) + " " + (str(e6.get())) + " " + (str(e7.get())) + " " + (str(e8.get())) + " " + (str(e9.get())))
    FirstRow = list(map(int, tempRow.split()))
    RowOne = FirstRow

    tempRow = ((str(e10.get())) + " " + (str(e11.get())) + " " + (str(e12.get())) + " " + (str(e13.get())) + " " + (str(e14.get())) + " " + (str(e15.get())) + " " + (str(e16.get())) + " " + (str(e17.get())) + " " + (str(e18.get())))
    SecondRow = list(map(int, tempRow.split()))
    RowTwo = SecondRow

    tempRow = ((str(e19.get())) + " " + (str(e20.get())) + " " + (str(e21.get())) + " " + (str(e22.get())) + " " + (str(e23.get())) + " " + (str(e24.get())) + " " + (str(e25.get())) + " " + (str(e26.get())) + " " + (str(e27.get())))
    ThirdRow = list(map(int, tempRow.split()))
    RowThr = ThirdRow

    tempRow = ((str(e28.get())) + " " + (str(e29.get())) + " " + (str(e30.get())) + " " + (str(e31.get())) + " " + (str(e32.get())) + " " + (str(e33.get())) + " " + (str(e34.get())) + " " + (str(e35.get())) + " " + (str(e36.get())))
    FourthRow = list(map(int, tempRow.split()))
    RowFou = FourthRow

    tempRow = ((str(e37.get())) + " " + (str(e38.get())) + " " + (str(e39.get())) + " " + (str(e40.get())) + " " + (str(e41.get())) + " " + (str(e42.get())) + " " + (str(e43.get())) + " " + (str(e44.get())) + " " + (str(e45.get())))
    FithRow = list(map(int, tempRow.split()))
    RowFiv = FithRow

    tempRow = ((str(e46.get())) + " " + (str(e47.get())) + " " + (str(e48.get())) + " " + (str(e49.get())) + " " + (str(e50.get())) + " " + (str(e51.get())) + " " + (str(e52.get())) + " " + (str(e53.get())) + " " + (str(e54.get())))
    SixthRow = list(map(int, tempRow.split()))
    RowSix = SixthRow

    tempRow = ((str(e55.get())) + " " + (str(e56.get())) + " " + (str(e57.get())) + " " + (str(e58.get())) + " " + (str(e59.get())) + " " + (str(e60.get())) + " " + (str(e61.get())) + " " + (str(e62.get())) + " " + (str(e63.get())))
    SeventhRow = list(map(int, tempRow.split()))
    RowSev = SeventhRow

    tempRow = ((str(e64.get())) + " " + (str(e65.get())) + " " + (str(e66.get())) + " " + (str(e67.get())) + " " + (str(e68.get())) + " " + (str(e69.get())) + " " + (str(e70.get())) + " " + (str(e71.get())) + " " + (str(e72.get())))
    EigthRow = list(map(int, tempRow.split()))
    RowEig = EigthRow

    tempRow = ((str(e73.get())) + " " + (str(e74.get())) + " " + (str(e75.get())) + " " + (str(e76.get())) + " " + (str(e77.get())) + " " + (str(e78.get())) + " " + (str(e79.get())) + " " + (str(e80.get())) + " " + (str(e81.get())))
    NinthRow = list(map(int, tempRow.split()))
    RowNin = NinthRow        

    print(RowOne)
#
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
                #solved.append((bo[i][j]))
                print(bo[i][j])
            else:
                #solved.append(str(bo[i][j]))
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

# Prints whole solved array
#   for x in range(len(board)): 
#       print (board[x])
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

# Top 3:
looper = 0
arrayModifier = 0

for x in range(3):

    mylabel = w.create_text((30), 30 + looper, text=board[0 + arrayModifier][0])
    mylabel = w.create_text((80), 30 + looper, text=board[0 + arrayModifier][1])
    mylabel = w.create_text((130), 30 + looper, text=board[0 + arrayModifier][2])

    mylabel = w.create_text((190), 30 + looper, text=board[0 + arrayModifier][3])
    mylabel = w.create_text((240), 30 + looper, text=board[0 + arrayModifier][4])
    mylabel = w.create_text((290), 30 + looper, text=board[0 + arrayModifier][5])

    mylabel = w.create_text((345), 30 + looper, text=board[0 + arrayModifier][6])
    mylabel = w.create_text((395), 30 + looper, text=board[0 + arrayModifier][7])
    mylabel = w.create_text((445), 30 + looper, text=board[0 + arrayModifier][8])

    looper = looper + 50
    arrayModifier = arrayModifier + 1

# Med 3:
looper = 155
arrayModifier = 3

for x in range(3):

    mylabel = w.create_text((30), 30 + looper, text=board[0 + arrayModifier][0])
    mylabel = w.create_text((80), 30 + looper, text=board[0 + arrayModifier][1])
    mylabel = w.create_text((130), 30 + looper, text=board[0 + arrayModifier][2])

    mylabel = w.create_text((190), 30 + looper, text=board[0 + arrayModifier][3])
    mylabel = w.create_text((240), 30 + looper, text=board[0 + arrayModifier][4])
    mylabel = w.create_text((290), 30 + looper, text=board[0 + arrayModifier][5])

    mylabel = w.create_text((345), 30 + looper, text=board[0 + arrayModifier][6])
    mylabel = w.create_text((395), 30 + looper, text=board[0 + arrayModifier][7])
    mylabel = w.create_text((445), 30 + looper, text=board[0 + arrayModifier][8])

    looper = looper + 50
    arrayModifier = arrayModifier + 1

# Bot 3:
looper = 310
arrayModifier = 6

for x in range(3):

    mylabel = w.create_text((30), 30 + looper, text=board[0 + arrayModifier][0])
    mylabel = w.create_text((80), 30 + looper, text=board[0 + arrayModifier][1])
    mylabel = w.create_text((130), 30 + looper, text=board[0 + arrayModifier][2])

    mylabel = w.create_text((190), 30 + looper, text=board[0 + arrayModifier][3])
    mylabel = w.create_text((240), 30 + looper, text=board[0 + arrayModifier][4])
    mylabel = w.create_text((290), 30 + looper, text=board[0 + arrayModifier][5])

    mylabel = w.create_text((345), 30 + looper, text=board[0 + arrayModifier][6])
    mylabel = w.create_text((395), 30 + looper, text=board[0 + arrayModifier][7])
    mylabel = w.create_text((445), 30 + looper, text=board[0 + arrayModifier][8])

    looper = looper + 50
    arrayModifier = arrayModifier + 1


#solve(board)
#print_board(board)

w.pack()

win.mainloop ()
