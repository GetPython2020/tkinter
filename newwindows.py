from tkinter import *

window = Tk()
window.title('window')

def open():
    top = Toplevel()
    top.title('top')
    label2 = Label(top, text='another window').pack()
    button2 = Button(top,text='close',command=top.destroy).pack()

button = Button(window,text='open new window', command=open).pack()
label = Label(window,text='this is the first window').pack()


window.mainloop()