import tkinter as tk

window = tk.Tk()

frame1 = tk.LabelFrame(window, text='this is my frame', padx=5, pady=5)
frame2 = tk.LabelFrame(window, text='this is my second frame', padx=5, pady=5)
frame1.pack(padx=10,pady=10)
frame2.pack()

window.mainloop()
