from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk()
window.title('code here')

def pick():
    global myimg
    window.filename = filedialog.askopenfile(initialdir="c:", title='choose your file', filetypes=(('png files', '*.png'), ('all file', '*.*')))
    loc = str(window.filename).split(' ')[1].split('=')[1].split('/')[-1][:-1]
    lable = Label(text=loc).pack()
    myimg = ImageTk.PhotoImage(Image.open(loc))
    mylabel = Label(image=myimg).pack()


button = Button(text='chose one pic',command=pick).pack()
window.mainloop()