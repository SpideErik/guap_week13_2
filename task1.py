from random import randint
from tkinter import *


def change(d):
    global width, height
    width += d
    height += d
    width = max(4, width)
    width = min(100, width)
    height = max(4, height)
    height = min(100, height)
    button.config(width=width, height=height, text=f'{width}x{height}')


root = Tk()
root.title('Button')
width = 4
height = 4
button = Button(text=f'{width}x{height}', font='Arial 24', width=width, height=height, command=lambda: change(1))
button.bind('<Button-3>', lambda e: change(-1))
button.pack()

root.mainloop()
