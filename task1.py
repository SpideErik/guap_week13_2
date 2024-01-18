from random import randint
from tkinter import *


def plus():
    global width, height
    if width < 100:
        width += 1
    if height < 100:
        height += 1
    button.config(width=width, height=height, text=f'{width}x{height}')


def minus():
    global width, height
    if width:
        width -= 1
    if height:
        height -= 1
    button.config(width=width, height=height, text=f'{width}x{height}')


root = Tk()
root.title('Button')
width = 4
height = 4
button = Button(text=f'{width}x{height}', font='Arial 24', width=width, height=height, command=plus)
button.bind('<Button-3>', lambda e: minus())
button.pack()

root.mainloop()
