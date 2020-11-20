from tkinter import *
top = Tk()

text_box = Text()
text_box.pack()

text_box.insert('1.0','book title')
text_box.insert('2.0', '\nTable of Content')
text_box.insert(END,'\nThe End')
print(text_box.get('1.0','1.4'))  #line number starts from 1, character number starts from 0, here get first line the first character to the fourth character
print(text_box.get('1.0',tk.END) # get all characters
text_box.delete(1.0) # delete the first character in the first line

top.mainloop()
