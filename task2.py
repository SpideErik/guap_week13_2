from random import randint
from tkinter import *


def press(x):
    x = randint(1, x)
    num.set(str(x))


root = Tk()
root.title('Button')
f = 'Arial 24'
num = StringVar()
Entry(textvariable=num, font=f, width=5).pack()
Button(text='от 1 до 6', font=f, command=lambda: press(6)).pack()
Button(text='от 1 до 20', font=f, command=lambda: press(20)).pack()

root.mainloop()
