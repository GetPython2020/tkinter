from tkinter import *
top = Tk()

text_box = Text()
text_box.pack()

text_box.insert('1.0','book title')
text_box.insert('2.0', '\nTable of Content')
text_box.insert(END,'\nThe End')
print(text_box.get('1.0','1.4'))

top.mainloop()
