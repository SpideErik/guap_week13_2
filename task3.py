from tkinter import *

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def press(clr):
    button.config(bg=clr, text=f'Выбран цвет:\n{clr}')


root = Tk()
root.title('Button')
f = 'Arial 24'

for i in colors:
    Button(text=i, bg=i, font=f, command=lambda x=i: press(x)).pack(expand=YES, fill=BOTH)

button = Button(text='Выбран цвет:\ngray', bg='gray', font=f, command=lambda: press('gray'))
button.pack(expand=YES, fill=BOTH)

root.mainloop()
