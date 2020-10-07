from tkinter import *

window = Tk()
window.title('your choices')

r = IntVar()
r.set(0)

Radiobutton(window,text='apple',variable=r,value=1).pack()
Radiobutton(window,text='banana',variable=r,value=2).pack()
Radiobutton(window,text='kiwi',variable=r,value=3).pack()

Button(window,text='next').pack()

window.mainloop()