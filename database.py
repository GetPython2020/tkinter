from tkinter import *
import sqlite3

window = Tk()
#create/connect to a database
conn = sqlite3.connect('information.db')
c = conn.cursor()

#create table (table created once runned the file, not need to run again when doing other revise)
# c.execute('''CREATE TABLE info(
#            first_name text,
#           last_name text,
#           zipcode integar) ''')

def submit():
    # create/connect to a database
    conn = sqlite3.connect('information.db')
    c = conn.cursor()

    first=fentry.get()
    last=lentry.get()
    zip=zentry.get()

    #insert input into database
    c.execute('INSERT INTO info VALUES(:fentry,:lentry,:zentry)',
              {'fentry':fentry.get(),
               'lentry':lentry.get(),
               'zentry':zentry.get()
              }
                )
    #clear all input
    fentry.delete(0,END)
    lentry.delete(0, END)
    zentry.delete(0, END)

    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('information.db')
    c = conn.cursor()

    c.execute('SELECT * FROM info')
    inf = c.fetchall()
    print_record=''
    for record in inf:
        print_record += str(record) + '\n'
    print(print_record)
    show_label = Label(text=print_record)
    show_label.grid(row=6,column=0,columnspan=2)  #前面用了grid，就不能再用pack了

    conn.commit()
    conn.close()

show_button = Button(text='show information',command=show).grid(row=4,column=0,columnspan=2)

flabel = Label(text='first_name').grid(row=0,column=0)
llabel = Label(text='last_name').grid(row=1,column=0)
ziplabel = Label(text='zipcode').grid(row=2,column=0)

fentry = Entry()
fentry.grid(row=0,column=1)
lentry = Entry()
lentry.grid(row=1,column=1)
zentry = Entry()
zentry.grid(row=2,column=1)

button = Button(text='submit into database',command=submit).grid(row=3, column=0, columnspan=2)

window.mainloop()