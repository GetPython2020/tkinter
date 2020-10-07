from tkinter import *

window = Tk()

days = StringVar()
day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
days.set(day_list[0])

box = OptionMenu(window,days,*day_list).pack()

def show():
    mylabel = Label(text=days.get()).pack()

button = Button(window,text='show value',command=show).pack()

window.mainloop()

