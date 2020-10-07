from tkinter import *

window = Tk()
window.geometry('400x400')

vertical = Scale(from_=0, to=1000)
vertical.pack(anchor=E)

horizontal = Scale(from_=0, to=1000, orient=HORIZONTAL)
horizontal.pack(anchor=W)

window.mainloop()