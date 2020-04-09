from tkinter import *


def win1():
    # this is the main/root window
    root = Tk()
    root.title("Window 1")
    startButton = Button(root, text="Start", command=win2)
    startButton.grid(row=9, column=7)
    leaveButton = Button(root, text="Quit", command=root.destroy)
    leaveButton.grid(row=1, column=1, sticky='nw')
    b1Var = StringVar()
    b2Var = StringVar()

    b1Var.set('b1')
    b2Var.set('b2')
    box1Label = Label(root, textvariable=b1Var, width=12)
    box1Label.grid(row=3, column=2)
    box2Label = Label(root, textvariable=b2Var, width=12)
    box2Label.grid(row=3, column=3)
    root.mainloop()


def win2():
    # this is the child window
    board = Toplevel()
    board.title("Window 2")
    s1Var = StringVar()
    s2Var = StringVar()
    s1Var.set("s1")
    s2Var.set("s2")
    square1Label = Label(board, textvariable=s1Var)
    square1Label.grid(row=0, column=7)
    square2Label = Label(board, textvariable=s2Var)
    square2Label.grid(row=0, column=6)


win1()