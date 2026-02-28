from tkinter import *
from datetime import datetime

root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#228B22')

lbl1 = Label(frame, text = "Name", bg = '#726E6D')
lbl2 = Label(frame, text = "Year", bg = '#726E6D')
lbl3 = Label(frame, text = "Month", bg = '#726E6D')
lbl4 = Label(frame, text = "Date", bg = '#726E6d')

name_entry = Entry(frame)
year_entry = Entry(frame)
month_entry = Entry(frame)
date_entry = Entry(frame)

def display():
    name = name_entry.get()
    year = int(year_entry.get())
    month = int(month_entry.get())
    date = int(date_entry.get())

    today = datetime.today()
    birth_date = datetime(year, month, date)

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    greet = "Hey "+name
    message = f"\nYou Are {age} years old"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg = '#000000', fg = 'white')

btn = Button(text = 'Calculate Age', command = display, bg = '#726E6D')

frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
year_entry.place(x=150,y=80)
lbl3.place(x=20, y=140)
month_entry.place(x=150,y=140)
lbl4.place(x=20, y=160)
date_entry.place(x=150, y=160)
btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()