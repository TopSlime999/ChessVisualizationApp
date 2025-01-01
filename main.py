from tkinter import *
import random
 
window = Tk()


def which_square(row, column):
    dict = {
        0:'a',
        1:'b',
        2:'c',
        3:'d',
        4:'e',
        5:'f',
        6:'g',
        7:'h'}
    
    dict2 = {
        0:8,
        1:7,
        2:6,
        3:5,
        4:4,
        5:3,
        6:2,
        7:1
    }
    print(row, dict2[row])
    if dict[column] + str(dict2[row]) == callout:
        print("correct")
        change_callout(rerun=True)
    else:
        print(dict[column] + str(dict2[row]) , callout)
        print("incorrect")
    change_callout(rerun=True)

def change_callout(rerun):
    global callout
    if rerun == True:
        callout = random.choice(list("abcdefgh")) + str(random.randint(1,8))
        square_label.config(text=f"{callout}")

callout = random.choice(list("abcdefgh")) + str(random.randint(1,8))
global square_label
square_label = Label(text=f"{callout}", font=('Arial', 40))
square_label.pack(side="top")
squares = [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],]

frame = Frame(window)
frame.pack()

for row in range(8):
    for column in range(8):
        print(row + column % 2 == 0)
        if (row % 2 != 0 and column % 2 != 0) or (row % 2 == 0 and column % 2 == 0):
            squares[row][column] = Button(frame, text='',relief=RAISED, border=1, width=8,height=4, bg='#f3e5ab', command=lambda row=row, column=column: which_square(row, column))
        else:
            squares[row][column] = Button(frame, text='',relief=RAISED, border=1, width=8,height=4, bg='black', command=lambda row=row, column=column: which_square(row, column))
        
        squares[row][column].grid(row=row, column=column)


window.mainloop()