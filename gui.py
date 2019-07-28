from tkinter import *
# Start of GUI

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
        mylabel = w.create_text((ROne * 50) - 20, 30, text=ROne)
        mylabel = w.create_text((ROne * 50) + 140, 30, text=ROne + 3)
        mylabel = w.create_text((ROne * 50) + 295, 30, text=ROne + 6)

        ROne += 1

RTwo = 1
for x in range(3):
        mylabel = w.create_text((RTwo * 50) - 20, 80, text=RTwo + 9)
        mylabel = w.create_text((RTwo * 50) + 140, 80, text=RTwo + 12)
        mylabel = w.create_text((RTwo * 50) + 295, 80, text=RTwo + 15)

        RTwo += 1

RThree = 1
for x in range(3):
        mylabel = w.create_text((RThree * 50) - 20, 130, text=RThree + 18)
        mylabel = w.create_text((RThree * 50) + 140, 130, text=RThree + 21)
        mylabel = w.create_text((RThree * 50) + 295, 130, text=RThree + 24)

        RThree += 1

RFour = 1
for x in range(3):
        mylabel = w.create_text((RFour * 50) - 20, 185, text=RFour + 27)
        mylabel = w.create_text((RFour * 50) + 140, 185, text=RFour + 30)
        mylabel = w.create_text((RFour * 50) + 295, 185, text=RFour + 33)

        RFour += 1

RFive = 1
for x in range(3):
        mylabel = w.create_text((RFive * 50) - 20, 235, text=RFive + 36)
        mylabel = w.create_text((RFive * 50) + 140, 235, text=RFive + 39)
        mylabel = w.create_text((RFive * 50) + 295, 235, text=RFive + 42)

        RFive += 1

RSix = 1
for x in range(3):
        mylabel = w.create_text((RSix * 50) - 20, 285, text=RSix + 45)
        mylabel = w.create_text((RSix * 50) + 140, 285, text=RSix + 48)
        mylabel = w.create_text((RSix * 50) + 295, 285, text=RSix + 51)

        RSix += 1

RSeven = 1
for x in range(3):
        mylabel = w.create_text((RSeven * 50) - 20, 340, text=RSeven + 54)
        mylabel = w.create_text((RSeven * 50) + 140, 340, text=RSeven + 57)
        mylabel = w.create_text((RSeven * 50) + 295, 340, text=RSeven + 60)

        RSeven += 1

REight = 1
for x in range(3):
        mylabel = w.create_text((REight * 50) - 20, 390, text=REight + 62)
        mylabel = w.create_text((REight * 50) + 140, 390, text=REight + 66)
        mylabel = w.create_text((REight * 50) + 295, 390, text=REight + 69)

        REight += 1

RNine = 1
for x in range(3):
        mylabel = w.create_text((RNine * 50) - 20, 440, text=RNine + 72)
        mylabel = w.create_text((RNine * 50) + 140, 440, text=RNine + 75)
        mylabel = w.create_text((RNine * 50) + 295, 440, text=RNine + 78)

        RNine += 1
#solve(board)
#print_board(board)

w.pack()

win.mainloop ()
