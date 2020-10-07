from tkinter import *

window = Tk()

var = [
    ('apple','hot people'),
    ('banana','peace people'),
    ('watermelon','calm people')]

v=StringVar()

for text, value in var:
    c=Checkbutton(window,text=text,variable=v,onvalue=value)
    c.pack()

def show():
    mylabel = Label(text=var.get()).pack()


mybutton = Button(window,text='show meaning',command=show).pack()

window.mainloop()


from tkinter import *

window = Tk()

v=StringVar()

c=Checkbutton(window,text='text',variable=v,onvalue='value')
c.pack()
c.deselect()

def show():
    mylabel = Label(text=v.get()).pack()


mybutton = Button(window,text='show meaning',command=show).pack()

window.mainloop()
