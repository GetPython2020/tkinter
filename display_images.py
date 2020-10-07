import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

window.title('Animals')

my_img1 = ImageTk.PhotoImage(Image.open('birds.png'))
my_img2 = ImageTk.PhotoImage(Image.open('duck.png'))
my_img3 = ImageTk.PhotoImage(Image.open('goldfish.png'))
my_img4 = ImageTk.PhotoImage(Image.open('chicken.png'))
imgs = [my_img1,my_img2,my_img3,my_img4]


def click_back(pic_num):

    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()

    my_label= tk.Label(image=imgs[pic_num-1])
    my_label.grid(row=0, column=0, columnspan=3)

    button_back = tk.Button(text='<<',command=lambda : click_back(pic_num-1))
    button_exit = tk.Button(text='close',command=window.quit)
    button_forward = tk.Button(text='>>',command=lambda:click_forward(pic_num+1))
    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)

def click_forward(pic_num):

    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()

    num = pic_num
    my_label = tk.Label(image=imgs[num - 1])
    my_label.grid(row=0, column=0, columnspan=3)

    button_back = tk.Button(text='<<', command=lambda:click_back(pic_num-1))
    button_exit = tk.Button(text='close', command=window.quit)
    button_forward = tk.Button(text='>>', command=lambda:click_forward(pic_num+1))
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)



my_label = tk.Label(image=imgs[0])
my_label.grid(row=0, column=0, columnspan=3)

button_back = tk.Button(text='<<', state=tk.DISABLED)
button_exit = tk.Button(text='close', command=window.quit)
button_forward = tk.Button(text='>>', command=lambda:click_forward(2))
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


window.mainloop()