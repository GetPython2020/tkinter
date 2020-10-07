from tkinter import *
from tkinter import messagebox

window = Tk()

def click():
    messagebox.showinfo('more info','there are more things to consider.')


Button(text='show more information',command=click).pack()

window.mainloop()